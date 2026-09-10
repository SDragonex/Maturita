+++
title = "PSP 22 – Datová vazba, rozhraní INotifyPropertyChange"
description = "Datová vazba, rozhraní INotifyPropertyChange – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 22
[extra]
author = "Dany Chaker"
cislo = 22
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

WPF binding propojuje zdrojovou hodnotu s vlastností cílového prvku. Zdroj často určuje `DataContext`, cestu `Path` a směr `Mode`. `OneWay` přenáší změny do UI, `TwoWay` umožní i zápis zpět. Rozhraní se v .NET jmenuje **`INotifyPropertyChanged`** s koncovým „d“; název tématu přebírá zkrácený školní zápis. Objekt implementující toto rozhraní vyvolává událost `PropertyChanged`, když se jeho vlastnost změní. Samotný setter bez oznámení nemusí UI obnovit. [Microsoft: oznámení změny vlastnosti](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-implement-property-change-notification).

`UpdateSourceTrigger` určuje, kdy se změna ze vstupu uloží do zdroje. U `TextBox.Text` je výchozí hodnota `LostFocus`, tedy aktualizace při ztrátě fokusu. Hodnota `PropertyChanged` zapisuje při každé změně textu; `Explicit` čeká na zavolání `UpdateSource()`. Tyto názvy označují režimy aktualizace vazby, nikoli rozhraní modelu. [Microsoft: aktualizace zdroje TextBoxu](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-control-when-the-textbox-text-updates-the-source). Validace má chránit model i vysvětlit chybu uživateli. Chybu vazby hledej také v diagnostickém výstupu.

## Praktický příklad

Navrhni vlastnost Jmeno, která po změně vyvolá PropertyChanged pro správný název. Navaž TextBox obousměrně a TextBlock jednosměrně. Porovnej zápis po každé změně se zápisem při ztrátě fokusu. Potom změň hodnotu přímo v modelu a ověř obrazovku.

## Časté chyby

Chybné jméno vlastnosti nebo DataContext může vazbu přerušit bez chyby při překladu. Oznámení kolekce není oznámení jejích položek.

## Otázky k procvičení

Co určuje Mode a co UpdateSourceTrigger? Proč používat nameof?

<details>
<summary>Kontrola odpovědi</summary>

`Mode` určuje směr toku, `UpdateSourceTrigger` okamžik zápisu do zdroje. Operátor `nameof` omezuje překlepy a pomáhá při přejmenování vlastnosti.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
