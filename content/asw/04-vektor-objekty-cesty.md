+++
title = "ASW 4 – Vektorová grafika – prostředí, nastavení, základní nástroje, objekty, cesty, vrstvy"
description = "Vektorová grafika – prostředí, nastavení, základní nástroje, objekty, cesty, vrstvy – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 4
[extra]
author = "Dany Chaker"
cislo = 4
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Vektorový editor ukládá objekty, jejich obrys, výplň a transformace. Obdélník nebo elipsa mají parametrický tvar; převod na cestu dovolí úpravu jednotlivých uzlů. Bézierova křivka je řízena kotevními body a táhly. Seskupení spojuje objekty pro manipulaci, sjednocení mění jejich geometrii. Booleovské operace zahrnují sjednocení, rozdíl a průnik. Vrstvy uspořádávají dokument. Zarovnání a rozložení dávají přesné vztahy mezi objekty; vodítka a přichytávání pomáhají při návrhu. Změna pořadí určuje překrytí, nikoli automaticky skutečný geometrický výřez.

## Praktický příklad

Sestav ikonu z kruhu a obdélníku. V jedné kopii objekty seskup, ve druhé sjednoť a ve třetí odečti kruh. U každé varianty zkus změnit kruh a vysvětli rozdíl mezi skupinou a výslednou cestou.

## Časté chyby

Příliš mnoho uzlů ztěžuje úpravu hladkých křivek. Bílý objekt přes jiný objekt není skutečný průhledný otvor.

## Otázky k procvičení

Kdy použiješ skupinu a kdy rozdíl cest? Co dělají táhla uzlu?

<details>
<summary>Kontrola odpovědi</summary>

Skupina zachová samostatné objekty, rozdíl vytvoří skutečný výřez. Táhla řídí tečnu a zakřivení přilehlého úseku.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
