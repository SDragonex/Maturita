+++
title = "PSP 14 – Struktura programu v C#, proměnné, základní typy dat, vstup a výstup, konzolová aplikace"
description = "Struktura programu v C#, proměnné, základní typy dat, vstup a výstup, konzolová aplikace – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 14
[extra]
author = "Dany Chaker"
cislo = 14
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

C# je staticky typovaný jazyk platformy .NET. Program může používat explicitní metodu Main nebo top-level statements podle verze a projektu. Proměnná má typ a hodnotu; var znamená odvození typu při překladu, nikoli libovolnou změnu typu za běhu. int ukládá celá čísla, double přibližná reálná čísla, decimal desetinné hodnoty s jinými vlastnostmi a bool logickou hodnotu. string reprezentuje text. Vstup z konzole je text nebo null, proto jej před výpočtem zpracuj. Operace celých čísel mohou oříznout desetinnou část. Formátování vstupu závisí také na kultuře.

## Praktický příklad

V metodě Main načti Console.ReadLine() a ověř int.TryParse(vstup, out int pocet). Pro záporný nebo nečíselný vstup zobraz vysvětlení. Vyzkoušej výraz 5 / 2 a 5 / 2.0: první vrátí 2, druhý 2,5 v číselné hodnotě double.

## Časté chyby

Parse může při chybném vstupu vyvolat výjimku. Var není totéž co dynamic. Console.ReadLine nemusí vrátit neprázdný text.

## Otázky k procvičení

Proč použít TryParse? Jak vypočítáš skutečný průměr dvou celých čísel?

<details>
<summary>Kontrola odpovědi</summary>

TryParse vrací informaci o úspěchu. Převeď operand na vhodný typ, například ((double)a + b) / 2, a zvaž rozsah vstupů.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
