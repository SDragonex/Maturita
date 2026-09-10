+++
title = "ASW 20 – Práce s tabulkovým procesorem"
description = "Práce s tabulkovým procesorem – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 20
[extra]
author = "Dany Chaker"
cislo = 20
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Buňka obsahuje hodnotu nebo vzorec; zobrazený formát není vždy skutečná uložená hodnota. Relativní odkaz se při kopírování posouvá, absolutní odkaz se znakem dolar zůstává pevný a smíšený fixuje řádek či sloupec. Funkce agregují nebo podmíněně vyhodnocují data. Filtrování skrývá část řádků, řazení mění pořadí. Kontingenční tabulka shrnuje větší seznam podle kategorií. Graf musí odpovídat otázce a typu dat. Ověření vstupů pomáhá zachovat platné hodnoty. Prázdná buňka, nula a text nula nemusí mít stejný význam.

## Praktický příklad

V řádku 2 máš množství v B2 a jednotkovou cenu v C2: vzorec =B2*C2 spočítá cenu. Sazbu přirážky ulož do F1 a ve vzorci =D2*(1+$F$1) ji při kopírování drž pevnou. Změň množství a ověř přepočet i součet.

## Časté chyby

Neřaď jen jeden sloupec nezávisle na zbytku záznamu. Desetinná čárka a oddělovače funkcí závisejí na prostředí.

## Otázky k procvičení

Co se změní při kopii B2 a $B$2 o řádek dolů? Proč nepoužít spojnicový graf pro libovolně seřazené kategorie?

<details>
<summary>Kontrola odpovědi</summary>

B2 se změní na B3, absolutní odkaz zůstane. Spojnice by sugerovala kontinuitu nebo trend, který data nemusí mít.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
