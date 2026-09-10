"""Check the study inventory and source links; this is not a factual review."""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = {
    'aj': (20, 'anglicky-jazyk', ['Osnova odpovědi', 'Slovníček EN / CZ', 'Modelový projev B1/B2', 'Gramatika a časté chyby']),
    'cjl': (97, 'cesky-jazyk-literatura', ['Rozsah četby', 'Autor a kontext', 'Kompozice a vyprávění', 'Postavy a jejich vztahy', 'Děj a hlavní motivy', 'Jazyk a styl', 'Otázky k ústní odpovědi']),
    'asw': (26, 'aplikacni-software', ['Co vysvětlit u zkoušky', 'Praktický příklad', 'Časté chyby', 'Otázky k procvičení']),
    'psp': (26, 'site-a-programovani', ['Co vysvětlit u zkoušky', 'Praktický příklad', 'Časté chyby', 'Otázky k procvičení']),
}


def read_page(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding='utf-8-sig')
    parts = text.split('+++', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'{path}: missing TOML front matter')
    return tomllib.loads(parts[1]), parts[2]


def check(root: Path = ROOT) -> list[str]:
    errors = []
    content = root / 'content'
    pages = {}
    for path in sorted(content.rglob('*.md')):
        rel = path.relative_to(content).as_posix()
        try:
            meta, body = read_page(path)
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
            continue
        pages[rel] = (meta, body)
        if not meta.get('title'):
            errors.append(f'{rel}: missing title')
        if re.search(r'Poznámky budou doplněny|\bTODO\b|lorem ipsum', body, re.I):
            errors.append(f'{rel}: unfinished placeholder')
        for target in re.findall(r'\]\(@/([^)]*)\)', body):
            destination = (content / target.split('#')[0]).resolve()
            if not destination.is_relative_to(content.resolve()) or not destination.is_file():
                errors.append(f'{rel}: broken source link @/{target}')
        if re.search(r'\]\(/(?!/)', body):
            errors.append(f'{rel}: root-relative link breaks subpath hosting')
    for subject, (count, index, headings) in SUBJECTS.items():
        items = [(path, value) for path, value in pages.items() if path.startswith(subject + '/') and not path.endswith('/_index.md')]
        numbers = []
        index_body = pages.get(f'posts/{index}.md', ({}, ''))[1]
        if len(items) != count:
            errors.append(f'{subject}: expected {count} topics, found {len(items)}')
        for path, (meta, body) in items:
            extra = meta.get('extra', {})
            number = extra.get('cislo')
            numbers.append(number)
            if type(number) is not int or meta.get('weight') != number or not Path(path).name.startswith(f'{number:02}-' if type(number) is int else '!'):
                errors.append(f'{path}: number/weight/filename mismatch')
            if extra.get('subject') != subject or extra.get('status') != 'study':
                errors.append(f'{path}: missing study metadata')
            for heading in headings:
                if f'## {heading}\n' not in body:
                    errors.append(f'{path}: missing {heading}')
            if len(re.findall(r'\w+', body, re.UNICODE)) < 100:
                errors.append(f'{path}: insufficient content for a study page')
            if f'(@/{path})' not in index_body:
                errors.append(f'{path}: missing from subject index')
        if sorted(n for n in numbers if type(n) is int) != list(range(1, count + 1)):
            errors.append(f'{subject}: numbering is not complete and unique')
    return errors


if __name__ == '__main__':
    issues = check()
    for issue in issues:
        print(issue)
    if not issues:
        print('Content OK: AJ 20, literature 97, ASW 26, PSP 26; 169 study pages.')
    sys.exit(bool(issues))
