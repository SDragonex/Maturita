+++
title = "ASW 10 – Blender – 3D animace"
description = "Blender – 3D animace – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 10
[extra]
author = "Dany Chaker"
cislo = 10
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

3D animace mění vlastnosti objektů, kamer, světel či kostry v čase. Klíčový snímek ukládá hodnotu na konkrétním snímku; křivka F-curve popisuje průběh. Konstantní interpolace skáče mezi stavy, lineární mění hodnotu rovnoměrně a Bézierova dovoluje plynulé rozjezdy. Rigging vytváří ovládací kostru, skinning váhy vztahu mezi kostmi a sítí. Kamera určuje kompozici, osvětlení čitelnost scény. Render animace do jednotlivých snímků umožňuje pokračovat po přerušení. Až následně lze snímky spojit do videa.

## Praktický příklad

Animuj pohyb krychle od x = 0 do x = 4 mezi snímky 1 a 49 při 24 fps. Mezi klíči uplynou 2 sekundy. Porovnej lineární a Bézierovu interpolaci a sleduj rychlost u krajů. Nastav rozsah exportu podle požadovaného počtu snímků.

## Časté chyby

Nezaměňuj počet snímků včetně obou krajů s časovým rozdílem mezi klíči. Zkontroluj aktivní kameru před dlouhým renderem.

## Otázky k procvičení

Jak obnovit přerušený render? Jak se změní pohyb při konstantní interpolaci?

<details>
<summary>Kontrola odpovědi</summary>

Při výstupu do obrazové sekvence dopočítej chybějící snímky. Konstantní interpolace drží hodnotu do dalšího klíče a pak ji skokem změní.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
