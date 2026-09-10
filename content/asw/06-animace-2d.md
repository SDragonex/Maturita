+++
title = "ASW 6 – 2D animace"
description = "2D animace – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 6
[extra]
author = "Dany Chaker"
cislo = 6
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Animace vytváří dojem pohybu ze změn obrazu v čase. Snímková frekvence určuje počet zobrazených snímků za sekundu. Klíčové snímky definují důležité stavy, mezisnímky mohou vzniknout ručně nebo interpolací. Frame-by-frame mění kresbu, tweening dopočítává polohu či jinou vlastnost. Timing určuje délku děje, spacing vzdálenost mezi polohami. Pozvolný rozjezd a dojezd jsou odlišné od konstantní rychlosti. Vrstvy oddělují postavu a pozadí; onion skin pomáhá porovnat sousední snímky. Smyčka musí navázat koncem na začátek.

## Praktický příklad

Navrhni dvousekundovou animaci míčku při 24 fps. Počítej 48 zobrazených snímků, rozvrhni odraz a dopad a zhušťuj polohy poblíž vrcholu. Zkontroluj, zda smyčka neobsahuje nechtěnou pauzu kvůli duplicitnímu krajnímu snímku.

## Časté chyby

Více fps samo o sobě neopraví špatný timing. Rovnoměrná změna pozice nevytvoří věrohodný pád pod gravitací.

## Otázky k procvičení

Jaký je rozdíl mezi timingem a spacingem? Kolik snímků má 5 sekund při 25 fps?

<details>
<summary>Kontrola odpovědi</summary>

Timing stanoví trvání, spacing průběh pohybu mezi polohami. Pět sekund obsahuje 125 snímků.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
