# Obsah a zdroje

Stav inventáře: 10. 9. 2026. Projekt obsahuje **169 studijních témat**. Počty jsou vlastností místních školních podkladů pro rok 2026, nikoli dosud potvrzeným rozsahem zkoušek 2027.

| Složka | Počet | Rozcestník | Podklad |
|---|---:|---|---|
| `content/aj/` | 20 | [Anglický jazyk](../content/posts/anglicky-jazyk.md) | [MZ-AJ.pdf](../static/MZ-AJ.pdf) |
| `content/cjl/` | 97 | [ČJL](../content/posts/cesky-jazyk-literatura.md) | [MZ-KNIHY.pdf](../static/MZ-KNIHY.pdf) |
| `content/asw/` | 26 | [Aplikační software](../content/posts/aplikacni-software.md) | [MZ-IT.pdf](../static/MZ-IT.pdf) |
| `content/psp/` | 26 | [Sítě a programování](../content/posts/site-a-programovani.md) | [MZ-IT.pdf](../static/MZ-IT.pdf) |

Každý rozcestník odkazuje na celou svou sadu. Soubory `_index.md` definují sekce a do počtu témat nepatří. Metodiky a rozcestníky v `content/posts/` jsou navíc.

## Platnost informací

| Druh údaje | Zdroj a způsob použití |
|---|---|
| Celostátní pravidla a termíny | MŠMT a CERMAT; konkrétní odkazy a datum kontroly jsou v [průvodci](../content/posts/jak-maturita-funguje.md) |
| Školní témata, seznam knih, formy zkoušek | Archivní PDF 2026; pro rok 2027 čekají na potvrzení aktuálními dokumenty [školy](https://www.sstebrno.cz/pro-studenty/maturity/) |
| Obecná osnova ústní zkoušky z ČJL | Místní dokument CERMAT/CZVV z roku 2014, verze 1.0; podklad pro budoucí strukturu rozborů, nikoli potvrzení školních podmínek 2027 |
| Literární fakta a interpretace | Především konkrétní přečtené vydání; bibliografie z katalogu, interpretace doložená ukázkou |
| Technické postupy | Dokumentace výrobce nebo specifikace pro použitou verzi; výsledek vlastního pokusu |
| Modelové odpovědi a studijní plán | Vlastní didaktické příklady a doporučení; nejsou školním zadáním ani údaji o studentovi |

Názvy témat samy nepotvrzují aktuální školní požadavky. Obecný odkaz na dokumentaci nebo knihovní katalog není zdrojem každého tvrzení v článku. Při opravě sporného údaje přidej konkrétní stránku, kapitolu nebo bibliografický záznam.

## Formát studijní stránky

Každý soubor má TOML metadata mezi oddělovači `+++`. `weight`, `extra.cislo` a číselný prefix názvu musí souhlasit. `extra.subject` je `aj`, `cjl`, `asw` nebo `psp`; `extra.status = "study"` označuje studijní obsah a není známkou schválení školou. Literatura navíc nese `school_category` převzatou ze školního seznamu.

```toml
+++
title = "ASW 1 – Základní pojmy z počítačové grafiky"
description = "Stručný popis tématu."
date = 2026-09-09
weight = 1
[extra]
cislo = 1
subject = "asw"
status = "study"
+++
```

Nadpis stránky vykresluje šablona; vlastní výklad začíná nadpisem druhé úrovně. Odkazy mezi články zapisuj pomocí Zoly, například `(@/posts/rozcestnik.md)`. Na současných dvouúrovňových adresách vede k PDF odkaz `../../MZ-IT.pdf`; po změně hloubky adresy je nutné jej upravit. Nepoužívej `/MZ-IT.pdf`, protože by přeskočil podcestu `/Maturita/`.

## Co má obsahovat jednotlivé téma

**AJ:** osnova odpovědi, slovníček EN/CZ, modelový projev B1/B2, otázky, gramatika a samostatný nácvik. Fiktivní zkušenosti musí zůstat označené. Modelová úroveň ani délka projevu nejsou potvrzeným školním limitem.

**ČJL, současný stav:** rozsah četby, autor a kontext, literární druh a žánr, kompozice a vyprávění, postavy a vztahy, děj a motivy, jazyk a otázky. U lyriky se nenutí románový děj a u výboru se děj titulní prózy nevydává za obsah celé knihy. Přehled doplňuje četbu; kompletní odborná revize všech 97 položek zatím není doložena. Přechod na novou osnovu níže je výslovně odložený a dosud neproběhl.

**ASW a PSP:** vysvětlení principu, praktický příklad, časté chyby, procvičení a samostatný úkol. Popis řešení není dokladem spuštění programu či konfigurace. U skutečně provedeného úkolu eviduj verzi nástroje, vstup, postup, očekávání a výsledek.

Od 10. 9. 2026 mají PSP 7 (IPv4) a PSP 21 (kolekce C#) konkrétní spuštěné ukázky a zkontrolované výstupy, viz [protokol](OVERENI.md). Výpočet adres nedokládá síťovou konektivitu a konzolové události nejsou testem vykreslení WPF. Další témata tím nejsou automaticky ověřena. Datum `updated` se u aktualizovaného článku zobrazuje v záhlaví a v metadatech změny.

**Maturitní práce:** společná metodika popisuje zadání, návrh, realizaci, dokumentaci, ověření a obhajobu. Konkrétní cíle, termíny a kritéria se doplní až podle schváleného zadání.

## Podklad pro budoucí sjednocení literárních rozborů

Uživatel přidal [obecna-struktura-ustni-zkousky.pdf](../static/obecna-struktura-ustni-zkousky.pdf). Soubor byl 10. 9. 2026 přečten textově i z náhledu stránky. Má jednu stranu, logo CERMAT a označení **CISKOM_3_1_6_P_struktura_UZ, © 2014 CZVV, verze 1.0**. Neobsahuje délku přípravy či zkoušení, bodové hodnocení ani údaj o platnosti pro rok 2027. Datum přidání souboru nezměnilo rok původního dokumentu.

Přesný seznam bodů je přepsaný v [metodice rozboru](../content/posts/rozbor-literatury.md). Budoucí rozbory mají zachovat toto členění:

| Část | Obsah podle dokumentu |
|---|---|
| Umělecký text I | Zasazení výňatku, téma a motiv, časoprostor, kompozice, literární druh a žánr |
| Umělecký text II | Vypravěč / lyrický subjekt, postava, vyprávěcí způsoby, typy promluv, veršová výstavba |
| Umělecký text III | Jazykové prostředky, tropy a figury včetně jejich funkce ve výňatku |
| Literárněhistorický kontext | Kontext autorovy tvorby a literární / obecně kulturní kontext |
| Neumělecký text I | Souvislost výňatků, hlavní myšlenka, podstatnost informací, způsoby čtení a interpretace, domněnky a fakta, komunikační situace |
| Neumělecký text II | Funkční styl, slohový postup a útvar, kompozice výňatku, jazykové prostředky a jejich funkce |

**Přepracování všech 97 rozborů je podle přání uživatele úkolem do budoucna.** Přidání PDF a metodiky není dokončenou migrací obsahu. Při pozdější úpravě se oddělí informace o díle od odpovědí závislých na konkrétním výňatku. Neumělecký text se nebude automaticky připisovat knize bez ukázky; vlastní nácvik musí být označen jako cvičný. Požadavky konkrétní školy pro jaro/podzim 2027 zůstávají samostatným ověřovaným vstupem.

## Literatura vyžadující upřesnění

Zvláštní pozornost vyžadují školní položky **15, 24, 29, 47 a 50**: sbírka versus jednotlivá báseň, různá vydání povídkových výborů nebo neurčený svazek cyklu. Každá stránka uvádí hranice svého přehledu. Školní kategorii zachovej, i pokud se liší od chronologického zařazení podle prvního vydání; případnou opravu kategorie musí podpořit nový školní podklad.

Pravidla výběru 20 knih v [metodice rozboru](../content/posts/rozbor-literatury.md) jsou převzata z podkladu 2025/2026. Bez školního seznamu 2027 a osobního výběru nelze potvrdit splnění požadavků konkrétního studenta.

## Postup obsahové revize

1. Vyber téma a zkontroluj shodu názvu a rozsahu se školním podkladem.
2. Ověř věcná tvrzení proti konkrétnímu zdroji; u literatury odliš vydání a filmovou adaptaci, u IT verzi nástroje.
3. Vyřeš otázky bez čtení vzorové odpovědi a zkontroluj výsledek. Nevyřešenou nejasnost pojmenuj přímo na stránce.
4. Doplň zdroj a podle rozsahu změny datum aktualizace. Do [protokolu](OVERENI.md) napiš rozsah provedené revize a její omezení.
5. Spusť kontrolu obsahu a sestavení. Kontrola počtu slov, nadpisů a souborů zachytí strukturální chyby, nikoli mylné vysvětlení nebo interpretaci.

Při přijetí školních podkladů 2027 aktualizuj současně příslušná PDF, rozcestníky, texty o platnosti, očekávané počty v `scripts/check_content.py` a tuto dokumentaci. Změny číslování nepřepisuj potichu: zachovej přehled, která původní položka odpovídá nové.

[Dokumentace](README.md) · [Plán](PLAN.md) · [Údržba](UDRZBA.md)
