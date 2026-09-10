# Maturita 2027

Studijní web pro **jaro a podzim 2027**, SŠTE Brno, Olomoucká, obor 18-20-M/01 Informační technologie. Obsah je v Markdownu, web sestavuje Zola a prohledávání zajišťuje Pagefind.

[Veřejná adresa webu](https://sdragonex.github.io/Maturita/) · [Dokumentace projektu](docs/README.md) · [Plán dokončení](docs/PLAN.md)

## Co projekt obsahuje

| Oblast | Rozsah | Vstup do obsahu |
|---|---:|---|
| Anglický jazyk | 20 témat | [Osnovy, slovní zásoba, modelové projevy a procvičení](content/posts/anglicky-jazyk.md) |
| Český jazyk a literatura | 97 položek | [Studijní přehledy ke školnímu seznamu](content/posts/cesky-jazyk-literatura.md) |
| Aplikační software | 26 témat | [Výklad, příklady a otázky](content/posts/aplikacni-software.md) |
| Počítačové sítě a programování | 26 témat | [Výklad, příklady a otázky](content/posts/site-a-programovani.md) |
| Maturitní práce | Metodika pro 7 oblastí | [Návrh, realizace, dokumentace a obhajoba](content/posts/maturitni-prace.md) |

Celkem jde o **169 studijních stránek** a společné průvodce. Literární přehledy jsou podkladem pro vlastní četbu a práci s ukázkou; nejsou úplnými rozbory všech vydání a dosud neprošly celoplošnou odbornou revizí učitelem. Modelové osobní odpovědi v AJ jsou fiktivní. Vlastní zadání maturitní práce v projektu není.

## Platnost pro rok 2027

MŠMT stanovilo jarní didaktické testy na **3.–6. května 2027**. Konkrétní den a čas každého předmětu z tohoto intervalu nevyplývá. Přesné podzimní termíny a školní rozpis pro rok 2027 zatím nejsou v projektu doloženy. [Sdělení MŠMT](https://msmt.gov.cz/media/wp-content/uploads/2025/11/Konkretni-terminy-jaro-2027.pdf).

Školní soubory [MZ-AJ.pdf](static/MZ-AJ.pdf), [MZ-KNIHY.pdf](static/MZ-KNIHY.pdf) a [MZ-IT.pdf](static/MZ-IT.pdf) jsou **archivní podklady pro rok 2026**. Jejich témata a číslování tvoří základ obsahu; platnost pro rok 2027 musí potvrdit aktuální dokumenty školy. Přihlášky, pravidla a zdroje se udržují v [průvodci maturitou](content/posts/jak-maturita-funguje.md), jehož poslední kontrola zdrojů je z 9. 9. 2026.

## Lokální sestavení

Potřebuješ **Python 3.11 nebo novější, Node.js s npm a Zolu 0.23.4**. CI používá Python 3.12 a Node.js 22. Pagefind je připnutý na verzi 1.5.2 a build jej spouští přes npm; první spuštění vyžaduje připojení k internetu.

1. Z [oficiálního vydání Zoly 0.23.4](https://github.com/getzola/zola/releases/tag/v0.23.4) stáhni archiv pro svůj systém.
2. Na Windows můžeš rozbalit `zola.exe` do `temp/tools/zola/zola.exe`, nastavit `ZOLA_EXE` nebo předat cestu argumentem `--zola`. Skript dále hledá Zolu na `PATH`.
3. V kořeni repozitáře spusť:

```powershell
py -3 scripts/build.py
```

Příkaz provede testy, kontrolu zdrojového obsahu, kontrolu Zoly, sestavení, indexaci Pagefind a kontrolu vygenerovaných odkazů a souborů. Při chybě se zastaví. Produkční výstup je v ignorované složce `public/` a používá `base_url` z `config.toml`.

Na systémech bez spouštěče `py` použij `python3 scripts/build.py`. Postup i řešení potíží popisuje [údržba a architektura](docs/UDRZBA.md). Výsledky skutečně provedených kontrol jsou odděleně v [protokolu ověření](docs/OVERENI.md).

## Náhled včetně vyhledávání

```powershell
py -3 scripts/build.py --preview
py -3 -m http.server 8765 --bind 127.0.0.1 --directory temp/preview
```

Otevři [lokální náhled](http://127.0.0.1:8765/Maturita/). Server ukonči pomocí `Ctrl+C`. Po změně obsahu znovu spusť sestavení náhledu. Samotný `zola serve` nevytvoří aktuální index Pagefind; HTML také neotvírej přímo přes `file://`.

## Struktura a úpravy

```text
content/aj/, cjl/, asw/, psp/  Jednotlivá studijní témata
content/posts/                Rozcestníky, pravidla a metodiky
templates/                    HTML šablony Tera
sass/                         Styly kompilované Zolou
static/                       PDF, obrázky a další kopírované soubory
scripts/                      Sestavení, validátory a testy
docs/                         Plán, obsahová pravidla a údržba
.github/workflows/main.yml    Kontrola a nasazení na GitHub Pages
```

Nové nebo opravené texty připravuj podle [pravidel obsahu a zdrojů](docs/OBSAH.md). Generované `public/`, pracovní `temp/` ani npm cache se neukládají do Gitu. Veřejnou verzi mění až nasazení; lokální úprava README nebo úspěšný build samy o sobě nic nepublikují.
