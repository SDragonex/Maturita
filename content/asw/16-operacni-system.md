+++
title = "ASW 16 – Operační systém – správa a ovládání operačního systému"
description = "Operační systém – správa a ovládání operačního systému – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 16
[extra]
author = "Dany Chaker"
cislo = 16
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

OS spravuje procesy, paměť, soubory, zařízení a uživatelské účty. Proces je spuštěný program s prostředky, vlákna představují vykonávání uvnitř procesu. Souborový systém organizuje data a metadata; přístupová práva určují oprávněné operace. Uživatelské rozhraní může být grafické i příkazové. Administrátorská oprávnění používej pro správu, ne automaticky pro vše. Ovladače propojují OS a hardware. Správa zahrnuje aktualizace, služby, úložiště, logy, účty a obnovu. Zjišťování problému začíná popisem příznaku a kontrolou vytížení, událostí a dostupného místa.

## Praktický příklad

Aplikace padá při otevření souboru. Zkontroluj, zda soubor existuje, zda má uživatel právo čtení, volné místo a co uvádí log aplikace. Porovnej malý známý soubor s problémovým a zaznamenej opakovatelné kroky.

## Časté chyby

Nespouštěj vše jako správce kvůli skrytí chyby práv. Ukončení procesu může ztratit neuložená data.

## Otázky k procvičení

Jak se liší proces a soubor programu? Proč je aktualizace a záloha jiný úkol?

<details>
<summary>Kontrola odpovědi</summary>

Soubor je uložený kód, proces jeho běžící instance. Aktualizace opravuje software, záloha umožňuje obnovu dat.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
