+++
title = "PSP 15 – Podmíněný příkaz if-else, switch"
description = "Podmíněný příkaz if-else, switch – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 15
[extra]
author = "Dany Chaker"
cislo = 15
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Podmíněný příkaz if provádí větev podle logického výrazu, else řeší opačný případ. Řetězec else if zkouší podmínky v pořadí; první vyhovující větev zabrání provedení dalších. Switch vybírá podle hodnoty nebo vzoru a hodí se pro přehledné rozdělení možností. Logické operátory AND a OR s krátkým vyhodnocováním dovolují nevyhodnotit druhou část, pokud je výsledek už známý. Porovnání a přiřazení jsou různé operace. U rozsahů promysli hraniční hodnoty a pořadí podmínek. Validaci vstupu odděl od vlastního rozhodování.

## Praktický příklad

Pro body 0 až 100 nejprve odmítni neplatný rozsah. Potom rozhodni: alespoň 80 výborný výsledek, alespoň 50 splněno, jinak nesplněno. Ověř 49, 50, 79, 80, -1 a 101. Jde o tréninkový příklad, ne maturitní hranice hodnocení.

## Časté chyby

Podmínka pro 50 a více před podmínkou pro 80 a více může pohltit vyšší větev. Samostatná if mohou provést více větví.

## Otázky k procvičení

Proč testovat právě hraniční hodnoty? Jak se liší if-if a if-else if?

<details>
<summary>Kontrola odpovědi</summary>

Na hranicích vznikají chyby zahrnutí. Dvě if se posoudí nezávisle, řetězec vybere nejvýše jednu odpovídající větev.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
