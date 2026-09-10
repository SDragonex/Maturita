+++
title = "PSP 16 – Cykly for, foreach, while, do-while"
description = "Cykly for, foreach, while, do-while – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 16
[extra]
author = "Dany Chaker"
cislo = 16
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

For spojuje inicializaci, podmínku a změnu řídicí proměnné. Foreach prochází prvky kolekce bez ručního indexování. While vyhodnocuje podmínku před tělem, do-while až po něm, takže tělo proběhne nejméně jednou. Break ukončí nejbližší cyklus, continue přeskočí zbytek jeho aktuální iterace. Cyklus potřebuje jasnou podmínku ukončení. Počet opakování a velikost vstupu určují časovou náročnost; vnořené průchody mohou práci výrazně násobit. Při změně kolekce během foreach může vzniknout výjimka nebo neplatný průchod podle typu kolekce.

## Praktický příklad

Spočítej součet pole pomocí foreach a ověř prázdné pole, jediný prvek a záporná čísla. Potom napiš for s podmínkou i < pole.Length. Pro opakované zadávání použij while a umožni ukončení i při konci vstupu.

## Časté chyby

Podmínka i <= Length přistoupí mimo poslední index. Cyklus čekající na platný vstup nesmí při trvalém null běžet navždy.

## Otázky k procvičení

Kdy použiješ do-while? Jak zajistíš ukončení cyklu?

<details>
<summary>Kontrola odpovědi</summary>

Pokud má tělo proběhnout před prvním testem. Měň stav směrem k ukončení a ošetři zvláštní případ konce vstupu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
