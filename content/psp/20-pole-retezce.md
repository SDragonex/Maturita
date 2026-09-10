+++
title = "PSP 20 – Pole jednorozměrné a vícerozměrné, řetězce"
description = "Pole jednorozměrné a vícerozměrné, řetězce – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 20
[extra]
author = "Dany Chaker"
cislo = 20
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Pole má pevný počet prvků a indexování od nuly. Poslední index je Length minus jedna. Dvourozměrné pole používá dvě souřadnice, jagged array je pole polí a může mít nestejně dlouhé řádky. String je neměnný: úprava vytváří nový řetězec. Řetězec může být null, prázdný nebo tvořený mezerami; jde o odlišné stavy. Délka string v C# počítá jednotky UTF-16, ne vždy uživatelsky vnímané znaky. Při zpracování textu zvaž kulturu a způsob porovnání. Větší skládání textu může využít StringBuilder.

## Praktický příklad

V poli najdi maximum: pro prázdný vstup nejprve rozhodni, jak oznámíš, že maximum neexistuje. U tabulky procházej rozměry přes GetLength. Pro jméno zkontroluj string.IsNullOrWhiteSpace a odstranění krajních mezer.

## Časté chyby

První prvek není na indexu 1. Neměnnost string neznamená, že proměnné nelze přiřadit jiný řetězec.

## Otázky k procvičení

Jak se liší obdélníkové a zubaté pole? Proč nelze délku textu vždy zaměnit za počet znaků?

<details>
<summary>Kontrola odpovědi</summary>

Obdélníkové má stejné rozměry, zubaté samostatná podpole. Některé znaky tvoří více jednotek UTF-16 nebo více kombinovaných znaků.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
