+++
title = "ASW 11 – 3D tisk"
description = "3D tisk – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 11
[extra]
author = "Dany Chaker"
cislo = 11
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

3D tisk vyrábí předmět po vrstvách. FDM/FFF ukládá roztavený filament, pryskyřičné technologie vytvrzují kapalný materiál světlem. Návrh musí respektovat rozměry, tloušťku stěn, přesahy, podpory a orientaci. Slicer převádí geometrii na dráhy zařízení a nastavuje vrstvu, výplň, stěny i podpory. STL ukládá trojúhelníkový povrch bez spolehlivě určených jednotek; 3MF může přenášet více informací. Uzavřená geometrie a správná orientace ploch omezují chyby. Pevnost bývá závislá na směru vrstev. Nastavení materiálu a bezpečné zacházení se řídí konkrétní tiskárnou a výrobcem.

## Praktický příklad

Navrhni držák s otvorem pro šroub a vůlí ověřenou malým zkušebním tiskem. V sliceru porovnej dvě orientace, spotřebu, podpory a směr namáhání. Prohlédni každou vrstvu před tiskem.

## Časté chyby

Pouhé zvýšení výplně nevyřeší nevhodnou orientaci nebo příliš tenké stěny. Nesahej na horké části a dodrž podmínky pro materiál.

## Otázky k procvičení

Proč vytisknout malý test tolerance? Co se stane po záměně mm a palců?

<details>
<summary>Kontrola odpovědi</summary>

Skutečný rozměr závisí na procesu a materiálu. Záměna jednotek změní rozměry faktorem 25,4.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
