+++
title = "ASW 1 – Základní pojmy z počítačové grafiky"
description = "Základní pojmy z počítačové grafiky – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 1
[extra]
author = "Dany Chaker"
cislo = 1
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Rastr ukládá obraz jako mřížku pixelů; vektor popisuje křivky a tvary matematicky. Fotografie bývá rastrová, logo se obvykle vytváří jako vektor. Rozměr v pixelech určuje množství obrazových dat, PPI vztah mezi pixely a fyzickou velikostí tisku. DPI je vlastnost tiskového výstupu. RGB skládá světlo, CMYK popisuje tiskové barvy; převod ovlivňuje barevný profil i zařízení. Barevná hloubka určuje počet možných hodnot. Ztrátová komprese zahazuje informace, bezeztrátová je uchová. JPEG je vhodný pro fotografie, PNG pro průhlednost a ostrou grafiku, SVG pro vektorové tvary.

## Praktický příklad

Fotografie 3000 × 2000 px vytištěná při 300 PPI má velikost 10 × 6,67 palce, tedy přibližně 25,4 × 16,9 cm. Pouhá změna údaje PPI nepřidá detaily. Nekomprimované RGB s 8 bity na kanál potřebuje 3000 × 2000 × 3 = 18 000 000 bajtů bez dalších dat.

## Časté chyby

Nezaměňuj MB s MiB ani změnu metadat s převzorkováním. Opakované ukládání JPEG může dále zhoršit obraz.

## Otázky k procvičení

Proč se logo při zvětšení SVG nemusí rozmazat? Spočítej velikost snímku 2400 px při 300 PPI.

<details>
<summary>Kontrola odpovědi</summary>

Vektor se znovu vykreslí z geometrie; vložená fotografie v SVG však zůstává rastrem. 2400 / 300 = 8 palců, tedy 20,32 cm.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
