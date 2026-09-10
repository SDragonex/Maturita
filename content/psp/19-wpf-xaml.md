+++
title = "PSP 19 – Tvorba uživatelského rozhraní, WPF, XAML – Button, Grid, Label, Textblock, TextBox, StackPanel"
description = "Tvorba uživatelského rozhraní, WPF, XAML – Button, Grid, Label, Textblock, TextBox, StackPanel – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 19
[extra]
author = "Dany Chaker"
cislo = 19
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

WPF vytváří desktopové rozhraní na Windows. XAML deklaruje strom prvků a jejich vlastnosti; C# zajišťuje chování nebo model. Grid rozděluje prostor do řádků a sloupců, StackPanel řadí prvky podél jedné osy. Button vyvolává akci, TextBox umožňuje zadávání, TextBlock zobrazuje text a Label může označit ovládací prvek. Layout prochází měřením a rozmístěním; pevné souřadnice často komplikují změnu velikosti. Datové vazby a příkazy umožňují oddělit logiku. Rozhraní potřebuje stavy chyb, čekání a prázdných dat. Dlouhá práce na UI vlákně blokuje reakce.

## Praktický příklad

Navrhni formulář se jménem, tlačítkem Uložit a chybovou zprávou. V Grid použij sloupec Auto pro popisek a hvězdičkový pro vstup. Změň velikost okna a zvětši systémové měřítko; ověř dostupnost všech prvků i klávesnicí.

## Časté chyby

TextBlock není vstupní pole. StackPanel nemusí rozdělit zbývající prostor jako Grid. Neprováděj dlouhé operace synchronně v obsluze kliknutí.

## Otázky k procvičení

Proč používat Grid místo pevných souřadnic? Jak poznáš zablokované UI vlákno?

<details>
<summary>Kontrola odpovědi</summary>

Grid se přizpůsobí obsahu a velikosti. Okno nereaguje na překreslení ani vstup, dokud se dlouhá operace nevrátí.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
