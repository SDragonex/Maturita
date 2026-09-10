# Údržba a architektura

Web je statický. Zola čte Markdown a TOML, vykresluje šablony Tera, kompiluje Sass a kopíruje `static/`. Pagefind následně indexuje výsledné HTML. Publikované stránky nepotřebují aplikační server ani databázi.

## Cesta od obsahu k webu

```text
content/ + config.toml + templates/ + sass/ + static/
                         │
                     Zola 0.23.4
                         │
                   vygenerované HTML
                         │
                   Pagefind 1.5.2
                         │
                 kontrola odkazů a souborů
                         │
                  public/ nebo lokální náhled
```

- `content/posts/` obsahuje rozcestníky, pravidla a metodiky; seznam příspěvků se stránkuje.
- `content/aj/`, `cjl/`, `asw/` a `psp/` mají sekce řazené podle `weight`. Jejich `_index.md` se samostatně nevykreslují, stránky používají `page.html`.
- `templates/_base.html` definuje rozložení, motiv, navigaci, vyhledávání a MathJax. `index.html` je úvodní stránka a `page.html` studijní článek s obsahem a navigací mezi tématy.
- `sass/style.scss` skládá dílčí styly. `static/` se kopíruje do kořene výsledného webu, proto `static/MZ-IT.pdf` odpovídá adrese `/Maturita/MZ-IT.pdf` při produkčním nasazení.
- Zola má vlastní vyhledávací index vypnutý. Pagefind indexuje obsah označený `data-pagefind-body`; navigace se vylučuje pomocí `data-pagefind-ignore`. Komponenta `pagefind-config` musí mít `bundle-path` i `base-url` sestavené pro aktuální podcestu včetně závěrečného lomítka.
- `data/links.toml` slouží stránce dalších projektů. Generování odběrů je vypnuté; související šablony a ovládání byly odstraněny.
- `static/js/study.js` přidává filtrování seznamů, zkratku „Přejít k seznamu“ a označení aktivního předmětu. Rozcestníky mají `extra.catalog` s kódem předmětu; tabulky a odkazy zůstávají dostupné i bez JavaScriptu. Filtr hledá v názvu, autorovi a čísle bez rozlišení diakritiky. Čistě číselný dotaz vybírá přesné existující číslo tématu, jinak hledá v textu (například název `1984`). Kategorie se přebírají z nadpisů tabulek. Tiskové styly zachovávají počet zobrazených výsledků i při aktivním filtru.
- `sass/_study.scss` sjednocuje tmavé vyhledávání, styly filtru a kompaktnější mobilní úvod. Dlouhé nadpisy zalamuje a široké tabulky na mobilu posouvá uvnitř vlastního bloku; rozbalená řešení mají odstavcové mezery. Volba motivu používá stávající lokální nastavení prohlížeče.

Šablony jsou upravené pro Tera v Zole 0.23.4. Změnu verze Zoly nebo Pagefind prováděj společně s kontrolou šablon, souborů vyhledávání a CI. Slepé přepnutí na nejnovější verzi není součástí běžného sestavení.

## Závislosti a sestavení

Vyžadovány jsou Python ≥ 3.11, Node.js s npm a Zola 0.23.4. CI používá Python 3.12 a Node.js 22. Instalace Zoly je popsána v [README](../README.md).

```powershell
py -3 scripts/build.py
```

Explicitní `--zola` má přednost před proměnnou `ZOLA_EXE`; zadaná cesta musí obsahovat požadovanou verzi. Bez obou nastavení se zkouší místní `temp/tools/zola/zola.exe`, jeho varianta `temp/tools/zola/zola` pro ostatní systémy a potom `PATH`. Příklad s vlastní cestou:

```powershell
py -3 scripts/build.py --zola "C:\Tools\zola\zola.exe"
```

Build používá Pagefind 1.5.2 přes npm a pracovní cache `temp/npm-cache`. Výstup je omezen na `public/`, `temp/preview/Maturita/`, `temp/root-site/` nebo vlastní podadresář `temp/builds/`. Opakované sestavení přepíše obsah zvolené výstupní složky; ukládej do ní pouze generovaný web. Cesty ke zdrojům, nástrojům a cache skript odmítne před spuštěním Zoly. Zdrojové Markdowny jsou verzované, generovaný web a pracovní soubory nikoli. Na Linuxu nahraď `py -3` za `python3`.

## Náhled pod stejnou podcestou jako produkce

```powershell
py -3 scripts/build.py --preview
py -3 -m http.server 8765 --bind 127.0.0.1 --directory temp/preview
```

Výstup se vytvoří v `temp/preview/Maturita/` s adresou [http://127.0.0.1:8765/Maturita/](http://127.0.0.1:8765/Maturita/). Server běží do `Ctrl+C`. Po úpravě obsahu opakuj první příkaz a obnov stránku. Pokud server již běží, sestavení proveď v druhém terminálu.

Vlastní cíl lze předat parametry `--base-url` a `--output-dir`. Pro ověření webu v kořeni například:

```powershell
py -3 scripts/build.py --base-url http://127.0.0.1:8766 --output-dir temp/root-site
py -3 -m http.server 8766 --bind 127.0.0.1 --directory temp/root-site
```

Použij [http://127.0.0.1:8766/](http://127.0.0.1:8766/). Adresa při sestavení musí odpovídat skutečné adrese náhledu, jinak mohou odkazy a vyhledávání směřovat na jiný web. Samotný `zola serve` nezajistí nový index Pagefind; přímé otevření HTML přes `file://` není podporovaný náhled vyhledávání.

## Co kontrolují skripty

| Kontrola | Účel a hranice |
|---|---|
| `test_*.py` | Regresní testy matematiky, sestavení a validátorů; nejde o věcnou kontrolu všech témat |
| `check_content.py` | TOML, soupis a číslování 169 témat, povinné části, zástupné texty, zdrojové odkazy a pokrytí rozcestníků |
| `zola check --skip-external-links` | Zpracování zdrojů a vnitřní odkazy; dostupnost cizích webů se tím nepotvrzuje |
| `zola build` a Pagefind | Vytvoření stránek a souborů vyhledávání |
| `check_site.py` | Místní odkazy, soubory, kotvy, jazyk, konfigurace vyhledávání a sousední témata |
| Prohlížeč | Skutečné ovládání, výsledky hledání, motiv, mobilní navigace, PDF a viditelné rozložení |

Absolutní odkazy na stejném hostiteli mimo `base_url`, například na jiné projekty účtu GitHub Pages, chápe validátor jako externí. Kořenová cesta `/tema/`, která opustí `/Maturita/`, je naopak chyba. Externí odkazy je potřeba kontrolovat samostatně.

Jednotlivé kontroly lze spustit při hledání chyby:

```powershell
py -3 -B -m unittest discover -s scripts -p "test_*.py" -v
py -3 scripts/check_content.py
py -3 scripts/check_site.py --site public --base-url https://sdragonex.github.io/Maturita
```

Samostatný validátor výstupu vyžaduje již sestavený web s indexem Pagefind. Po změně HTML nebo obsahu proto nepoužívej starý výstup jako důkaz kontroly nové verze.

Do [protokolu ověření](OVERENI.md) zapisuj datum, prostředí, spuštěný příkaz, výsledek a omezení. Počet úspěšných testů není ukazatelem věcné správnosti studijních textů.

## Matematické zápisy

`scripts/process_math.py` chrání interpunkci TeXu před Markdownem. Zachovává hranice odstavců, vynechává kód a jeho opakované použití nemá text dále měnit. `wrap_math.py` je kompatibilní vstup do stejného zpracování.

Nejprve zkontroluj konkrétní soubor bez zápisu:

```powershell
py -3 scripts/process_math.py --check content/psp/07-ip-adresovani.md
```

Bez `--check` skript zapisuje změny. Před hromadným použitím zkontroluj rozdíl v Gitu a zachovej testy odstavců, kódu, escapování a opakovaného zpracování. Samotná dostupnost MathJaxu ještě nepotvrzuje správné vykreslení konkrétního vzorce v prohlížeči.

## GitHub Pages

Workflow `.github/workflows/main.yml` kontroluje pull requesty do `main` a sestavuje web při změně větve `main` nebo ručním spuštění. Sdílený `build.py` používá pro produkci i ověření adres v kořeni webu. Publikační job používá artefakt výsledného `public/`; u pull requestu se veřejná verze nenasazuje. Repozitář musí mít GitHub Pages nastavené na GitHub Actions.

Produkční podcesta vychází z `config.toml`: `https://sdragonex.github.io/Maturita`. Při přejmenování repozitáře nebo vlastní doméně změň konfiguraci a zopakuj kontrolu odkazů, PDF a vyhledávání. Úspěšné místní sestavení neznamená, že byla změna odeslána nebo nasazena.

## Běžné potíže

| Projev | Postup |
|---|---|
| `zola` nefunguje kvůli odkazu WinGet nebo není na `PATH` | Použij skutečný rozbalený soubor přes `--zola` nebo `temp/tools/zola/zola.exe` |
| Python nezná `tomllib` | Spusť Python 3.11 nebo novější |
| npm hlásí chybu cache nebo chybí `npx` | Ověř instalaci Node.js/npm; sestavuj přes `build.py`, který používá projektovou cache |
| Hledání chybí nebo vrací starý obsah | Zopakuj celý build s Pagefind a použij HTTP náhled |
| PDF vede mimo `/Maturita/` | Oprav kořenový odkaz podle hloubky stránky a spusť kontrolu vygenerovaného webu |
| Chybí fonty, ikony nebo matematika | Zkontroluj přístup k CDN; fonty, Font Awesome a MathJax se načítají z internetu |

Web nepředstírá plnou dostupnost bez připojení: články a Pagefind jsou součástí sestaveného výstupu, ale externí typografie, ikony a vykreslení matematiky závisejí na dostupnosti příslušných služeb.

[Dokumentace](README.md) · [Obsah a zdroje](OBSAH.md) · [Plán](PLAN.md)
