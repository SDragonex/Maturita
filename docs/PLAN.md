# Plán dokončení a kontrola kvality

Výchozí audit: 8. 9. 2026. Aktualizace plánu: 10. 9. 2026. Cíl stanovený uživatelem: dokončit a průběžně dokumentovat studijní web pro **jaro a podzim 2027**, SŠTE Brno, Olomoucká, obor 18-20-M/01 Informační technologie.

## Výchozí problémy

Původní audit zjistil zástupné texty v AJ a literatuře, chybějící výklady obou odborných předmětů, neověřené školní podrobnosti v průvodci a problémy při publikaci do `/Maturita/`. Bylo potřeba sjednotit Zolu, vyhledávání, navigaci, sestavení a dokumentaci. Historické počty testů z auditu nejsou důkazem aktuálního stavu.

## Stav jednotlivých etap

| Etapa | Připravený výsledek | Co zbývá |
|---|---|---|
| Pravidla a zdroje | Průvodce 2027 odděluje celostátní pravidla od školních podkladů 2026; doložen interval jarních testů 3.–6. 5. 2027 | Doplnit podzimní termíny, schéma jednotlivých testů a školní dokumenty 2027 po zveřejnění |
| Angličtina | Všech 20 témat má osnovu, slovníček, modelový projev a procvičení | Věcná a jazyková revize, zpřesňování podle školních pracovních listů |
| Odborné předměty | 26 ASW a 26 PSP témat obsahuje výklad, praktický příklad a otázky; PSP 7 a 21 mají spuštěné ukázky s ověřeným výstupem | Rozšiřovat ověřené příklady o další témata; ověřit datovou vazbu také v okně WPF |
| Literatura | Všech 97 položek má přehled, rozsah četby, kontext, kompozici, postavy, děj, jazyk a otázky | Revize podle vydání, potvrzení rozsahu výborů a cyklů, rozpracování vlastního výběru 20 knih |
| Budoucí osnova literatury | Přidané PDF CERMAT/CZVV (2014, verze 1.0) je přečtené a jeho osnova zapsaná v metodice | **Na přání uživatele odloženo:** pozdější přepracování všech 97 rozborů; současné přehledy této osnově dosud nejsou sjednoceny |
| Maturitní práce | Metodika od zadání po obhajobu, osnova dokumentace a vzor ověření | Doplnit podle skutečného schváleného zadání, vedoucího a školních pokynů |
| Navigace a dokumentace | Úvod s předměty, přímá navigace, studijní plán, dokumentace a ověření ovládání na počítači i mobilní šířce | Dále ověřovat při změnách šablon; nejde o úplný audit přístupnosti |
| Technické dokončení | Zola 0.23.4, Pagefind 1.5.2, 22 úspěšných testů a místní sestavení pro produkci, kořen i podcestu | Vzdálené nasazení zatím neprovedeno; výsledky a omezení jsou v `OVERENI.md` |

„Připravený“ znamená, že výstup existuje v projektu. Samotný počet souborů nebo úspěšný technický test nepotvrzuje správnost každé věty učebního textu. Stav ověření se přebírá výhradně z [protokolu](OVERENI.md).

## Aktuální etapa — vzhled, navigace a podklady

Dokončeno místně 10. 9. 2026:

- RSS a Atom jsou vypnuté; odstraněné jsou nabídky, odkazy v hlavičce, obsluha a šablony odběrů. Validátor odmítne znovu vytvořený soubor odběru.
- Tmavý motiv používá pozadí `#0b0c0e`, tmavší tabulky, ovládání a výsledky vyhledávání.
- Všechny čtyři seznamy témat lze filtrovat podle textu, autora nebo čísla bez rozlišení diakritiky. Literatura a PSP mají také výběr kategorie, všechny seznamy počet výsledků a obnovení celého seznamu.
- Odkaz „Přejít k seznamu“ přeskočí úvodní pravidla. Obsah stránky umí při skoku odkrýt kategorii skrytou filtrem. Bez JavaScriptu zůstávají všechny položky dostupné.
- Navigace označuje aktuální předmět a téma uvádí svou pozici v seznamu. Úvod článku je na mobilu kompaktnější.
- Tiskové styly vynucují světlý motiv a zachovávají počet filtrovaných výsledků; úplná kontrola tisku zůstává dalším úkolem.

Aktuální kontrola zahrnuje 22 testů, tři sestavení, kontrolu odstraněných odběrů a ovládání v prohlížeči. Konkrétní případy a hranice ověření jsou v [protokolu](OVERENI.md), v záznamu z 10. 9. 2026.

Nově dodaný dokument [Obecná struktura ústní zkoušky](../static/obecna-struktura-ustni-zkousky.pdf) je zahrnutý v [metodice](../content/posts/rozbor-literatury.md) a [evidenci obsahu](OBSAH.md). Původní dokument nese rok 2014 a neurčuje platnost pro jaro/podzim 2027; není náhradou aktuálních školních podmínek.

## Odložená etapa — všech 97 literárních rozborů

Uživatel výslovně požaduje upravit rozbory podle nového podkladu **až v budoucnu**. Tato etapa se nyní nespouští. Budoucí postup:

1. Připravit společný formát se třemi částmi analýzy uměleckého textu, literárněhistorickým kontextem a dvěma částmi analýzy neuměleckého textu, přesně podle bodů v metodice.
2. Oddělit údaje o celém díle od rozboru konkrétního výňatku; nácvik s vlastním uměleckým či neuměleckým textem označit jako cvičný.
3. Při zpracování jednotlivých titulů ověřit vydání, rozsah četby, fakta a příklady. Nerelevantní body vysvětlit podle druhu textu, nevymýšlet například veršovou výstavbu prózy.
4. Postupně převést všech 97 přehledů, evidovat skutečně revidované položky a teprve potom aktualizovat pravidla strukturální kontroly.

Dokončení této budoucí etapy nelze odvozovat z nynějšího přidání PDF, úprav metodiky ani počtu existujících přehledů.

## Další postup podle priority

Z kontroly použitelnosti vycházejí dvě konkrétní další úpravy:

- **Řešené odborné příklady:** IPv4 (PSP 7) a kolekce C# (PSP 21) mají od 10. 9. postup, očekávaný výstup, varianty k procvičení a provedené ověření. Další krok je datová vazba WPF s kontrolou skutečné změny v okně; konzolový test událostí ji nenahrazuje. Ostatní příklady je potřeba ověřit postupně.
- **Tisk pro studium:** ověřit světlý výstup, tabulky a dlouhé články; navrhnout tisk s kontrolními odpověďmi a po tisku obnovit stav rozbalených částí. Zatím není ověřen kompletní tiskový tok.

Průběžné obsahové a provozní kroky:

1. Místní technické ověření je uzavřené v rozsahu protokolu. Při dalších úpravách udržet testy, produkční build, vyhledávání a podporu kořene i podcesty průchozí.
2. Provádět obsahovou revizi po jednotlivých předmětech. U oprav uvádět konkrétní zdroj, vydání nebo ověřený příklad; automatický validátor nenahrazuje tuto revizi. Hromadné přepracování literárních rozborů podle nové osnovy ponechat do výše uvedené odložené etapy.
3. Po získání školních podkladů 2027 porovnat názvy, číslování, rozsah, kritéria a termíny. Rozdíly promítnout do rozcestníků, témat, validátoru a dokumentace v jedné změně.
4. Po dodání osobního výběru knih zkontrolovat jeho soulad s potvrzenými pravidly školy a doplnit rozbory konkrétních vydání a ukázek.
5. Po dodání zadání maturitní práce vytvořit konkrétní harmonogram a kritéria splnění. Stav práce dokládat skutečnými výstupy a testy.
6. Před jarním i podzimním termínem znovu ověřit rozpis školy a MŠMT/CERMAT; zkontrolovat i pravidla pro případné opravné a náhradní zkoušky.

## Kritéria dokončení

- Každé převzaté školní téma má použitelný výklad, příklad nebo práci s textem a úkol k samostatné odpovědi.
- Školní požadavky mají dohledatelný zdroj a uvedený rok platnosti; nepotvrzené údaje zůstávají označené.
- Osobní zkušenosti modelových odpovědí nejsou vydávány za údaje o studentovi; metodika práce není vydávána za schválené zadání.
- Počty, číslování, odkazy a povinné části kontroluje skript; věcná revize má samostatný záznam.
- Web lze sestavit podle README a používat včetně vyhledávání pod správnou podcestou.
- Protokol uvádí skutečně provedené kontroly, jejich výsledek a zbývající omezení.

## Vstupy, které zatím chybí

Rok přípravy je **2027** a nevyžaduje další potvrzení. Otevřené zůstávají:

- Školní seznamy, kritéria a konkrétní rozpis pro rok 2027.
- Osobní výběr 20 knih včetně vydání; nejde o podmínku tvorby obecného webu.
- Upřesnění rozsahu nejednoznačných položek literatury, zejména čísel 15, 24, 29, 47 a 50.
- Vlastní schválené zadání maturitní práce a pokyny k odevzdání.

Publikace a práce s Gitem se oddělují od lokálních úprav. Tento plán sám nedokládá vytvoření commitu ani nasazení nové veřejné verze.

[Dokumentace](README.md) · [Obsah a zdroje](OBSAH.md) · [Údržba](UDRZBA.md) · [Ověření](OVERENI.md)
