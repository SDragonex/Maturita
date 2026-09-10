+++
title = "ASW 8 – Blender – objektový a editační mód, transformace, tvorba 3D modelů"
description = "Blender – objektový a editační mód, transformace, tvorba 3D modelů – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 8
[extra]
author = "Dany Chaker"
cislo = 8
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Objektový mód mění transformaci celého objektu, editační mód geometrii mesh: vrcholy, hrany a plochy. Posun, rotace a měřítko mohou být vyjádřeny v globálních či lokálních osách. Počátek objektu ovlivňuje transformace a některé modifikátory. Extrude vytváří navazující geometrii, inset vnitřní oblast plochy a loop cut přidává smyčku hran. Topologie určuje možnosti další úpravy i deformace. Normála popisuje orientaci plochy. Hladké stínování mění vzhled, nikoli skutečný počet polygonů. Měřítko modelu přizpůsob účelu a kontroluj rozměry.

## Praktický příklad

Vymodeluj stůl z desky a čtyř nohou. Nastav rozměry, rozliš změnu měřítka objektu a změnu souřadnic vrcholů. Pro další operace podle potřeby aplikuj měřítko a ověř, že objekt má očekávanou velikost.

## Časté chyby

Nevytvářej nechtěné duplicitní vrcholy opakovaným extrude bez posunu. Nespoléhej na hladké stínování jako opravu špatné geometrie.

## Otázky k procvičení

Jak se liší Object Mode a Edit Mode? Proč kontrolovat normály?

<details>
<summary>Kontrola odpovědi</summary>

První mění objekt jako celek, druhý jeho geometrii. Obrácené normály mohou způsobovat problémy se zobrazením i výrobou.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
