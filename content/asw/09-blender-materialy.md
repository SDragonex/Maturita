+++
title = "ASW 9 – Blender – materiály, textury, modifikátory"
description = "Blender – materiály, textury, modifikátory – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 9
[extra]
author = "Dany Chaker"
cislo = 9
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Materiál popisuje reakci povrchu na světlo; textura dodává prostorově proměnlivé hodnoty. UV mapa přiřazuje povrchu souřadnice obrázku. Shader používá například základní barvu, roughness a metallic. Drsnost mění rozptýlení odrazu, kovovost charakter povrchu. Normal mapa upravuje interpretovanou normálu pro stínování; sama nemění obrys modelu. Modifikátory upravují objekt podle pravidel: Mirror zrcadlí, Bevel sráží hrany, Subdivision Surface zjemňuje tvar. Jejich pořadí může změnit výsledek. Nedestruktivní řetězec uchovává původní síť, aplikování změnu zapíše do geometrie.

## Praktický příklad

Vytvoř bednu. Na jednu kopii použij Mirror a Bevel, druhou nech bez nich. Rozbal UV, přidej texturu dřeva a ověř orientaci na všech stěnách. Přesuň projekt na jiné místo a ověř dostupnost textur.

## Časté chyby

Barvová textura a mapa dat nemusí používat stejný barevný prostor. Nezaměňuj roughness s velikostí fyzických nerovností.

## Otázky k procvičení

Proč záleží na pořadí modifikátorů? Co normal mapa sama nezmění?

<details>
<summary>Kontrola odpovědi</summary>

Každý zpracovává výstup předchozího. Normal mapa sama neposune vrcholy ani nezmění siluetu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
