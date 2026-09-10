+++
title = "PSP 21 – Dynamické datové struktury – List, ObservableCollection, Dictionary"
description = "Dynamické datové struktury – List, ObservableCollection, Dictionary – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 21
[extra]
author = "Dany Chaker"
cislo = 21
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

`List<T>` je dynamický seznam s pořadím a indexy. `Dictionary<TKey, TValue>` mapuje jedinečné klíče na hodnoty; rychlé vyhledávání závisí na hashování a správném porovnání klíčů. `ObservableCollection<T>` oznamuje změny struktury kolekce a hodí se pro navázané WPF seznamy. Sama však neoznamuje změny vlastností uvnitř každého prvku; to musí řešit objekt. Generika zachovávají typovou informaci. Volba kolekce vychází z operací: přístup podle klíče, pořadí, vkládání či notifikace. Běžné kolekce automaticky nezaručují bezpečné souběžné zápisy.

## Praktický příklad

Pro katalog použij `Dictionary<int, Kniha>` a `TryGetValue` pro vyhledání. Pro viditelný seznam v okně použij `ObservableCollection<Kniha>`. Otestuj přidání knihy i změnu názvu existující knihy; jde o dva různé druhy oznámení.

## Časté chyby

Duplicita klíče a chybějící klíč mají odlišný význam. Nečekej, že ObservableCollection sama obnoví změněný název objektu.

## Otázky k procvičení

Kdy zvolit List a kdy Dictionary? Co musí oznamovat prvek navázané kolekce?

<details>
<summary>Kontrola odpovědi</summary>

`List` pro pořadí a průchod, `Dictionary` pro vyhledání podle klíče. Prvek musí oznamovat změny vlastností, typicky přes `INotifyPropertyChanged` a událost `PropertyChanged`; viz [příklad Microsoftu](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-implement-property-change-notification).

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
