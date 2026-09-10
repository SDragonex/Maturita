"""Build and validate the complete site, including the Pagefind index."""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
ZOLA_VERSION = '0.23.4'
PAGEFIND_VERSION = '1.5.2'


def run(command: list[str]) -> None:
    print('+ ' + ' '.join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def find_zola(explicit: str | None) -> str:
    configured = explicit or os.environ.get('ZOLA_EXE')
    candidates = [configured] if configured else [
        str(ROOT / 'temp/tools/zola/zola.exe'),
        str(ROOT / 'temp/tools/zola/zola'),
        shutil.which('zola'),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            result = subprocess.run([candidate, '--version'], capture_output=True, text=True, check=True)
            if result.stdout.strip() == f'zola {ZOLA_VERSION}':
                return candidate
        except (OSError, subprocess.CalledProcessError):
            continue
    raise ValueError(f'Zola {ZOLA_VERSION} is required. Set ZOLA_EXE or use --zola PATH. See README.md.')


def output_path(value: str) -> Path:
    path = (ROOT / value).resolve()
    # Zola cleans its output directory. Never let a CLI typo target source files.
    fixed_outputs = {ROOT / 'public', ROOT / 'temp/preview/Maturita', ROOT / 'temp/root-site'}
    build_root = ROOT / 'temp/builds'
    if path not in fixed_outputs and not (path != build_root and path.is_relative_to(build_root)):
        raise ValueError('Output must be public, temp/preview/Maturita, temp/root-site, or a subdirectory of temp/builds.')
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zola', help='Path to the Zola 0.23.4 executable')
    parser.add_argument('--base-url', help='Override the configured base URL')
    parser.add_argument('--output-dir', help='public, temp/preview/Maturita, temp/root-site, or a subdirectory of temp/builds')
    parser.add_argument('--preview', action='store_true', help='Build for http://127.0.0.1:8765/Maturita in temp/preview/Maturita')
    args = parser.parse_args()
    try:
        zola = find_zola(args.zola)
        npx = shutil.which('npx.cmd' if os.name == 'nt' else 'npx')
        if not npx:
            raise ValueError('Node.js with npm/npx is required. See README.md.')
        config = tomllib.loads((ROOT / 'config.toml').read_text(encoding='utf-8'))
        base_url = args.base_url or ('http://127.0.0.1:8765/Maturita' if args.preview else config['base_url'])
        if urlsplit(base_url).scheme not in ('http', 'https') or not urlsplit(base_url).netloc:
            raise ValueError('--base-url must be an absolute HTTP(S) URL.')
        output = output_path(args.output_dir or ('temp/preview/Maturita' if args.preview else 'public'))
        run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts', '-p', 'test_*.py', '-v'])
        run([sys.executable, '-B', 'scripts/check_content.py'])
        run([zola, 'check', '--skip-external-links'])
        run([zola, 'build', '--force', '--base-url', base_url, '--output-dir', str(output)])
        run([npx, '--cache', str(ROOT / 'temp/npm-cache'), '--yes', f'pagefind@{PAGEFIND_VERSION}', '--site', str(output)])
        run([sys.executable, '-B', 'scripts/check_site.py', '--site', str(output), '--base-url', base_url])
        print(f'Build and validation passed: {output}', flush=True)
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'Build failed: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
