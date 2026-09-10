+++
title = "PSP 21 – Dynamické datové struktury – List, ObservableCollection, Dictionary"
description = "Dynamické datové struktury – List, ObservableCollection, Dictionary – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
updated = 2026-09-10
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

Následující konzolový program ukazuje tři různé úlohy: pořadí v `List`, vyhledání knihy podle ID v `Dictionary` a oznámení změn v `ObservableCollection`. Události vypisuje do konzole, takže lze sledovat rozdíl mezi přidáním položky a změnou jejího názvu ještě před vytvořením okna WPF.

V nové prázdné pracovní složce vytvoř projekt pomocí .NET 10 SDK:

```powershell
dotnet new console -n Kolekce -f net10.0
cd Kolekce
```

Nahraď celý obsah `Program.cs` následujícím kódem a spusť `dotnet run`:

```csharp
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;

var nazvy = new List<string> { "Duna", "1984" };
Console.WriteLine($"List[0]: {nazvy[0]}");

var kniha = new Kniha("Duna");
var katalog = new Dictionary<int, Kniha> { [1] = kniha };
var seznam = new ObservableCollection<Kniha>();

seznam.CollectionChanged += (_, e) =>
    Console.WriteLine($"Kolekce: {e.Action}");
kniha.PropertyChanged += (_, e) =>
    Console.WriteLine($"Vlastnost: {e.PropertyName}");

seznam.Add(kniha);
if (katalog.TryGetValue(1, out var nalezena))
    Console.WriteLine($"ID 1: {nalezena.Nazev}");
if (!katalog.TryGetValue(2, out _))
    Console.WriteLine("ID 2 nenalezeno");

Console.WriteLine($"Druhý zápis ID 1: {katalog.TryAdd(1, new Kniha("1984"))}");
kniha.Nazev = "Duna (opravený název)";
kniha.Nazev = "Duna (opravený název)";
Console.WriteLine($"Katalog po změně: {katalog[1].Nazev}");
seznam.Remove(kniha);

public sealed class Kniha : INotifyPropertyChanged
{
    private string _nazev;
    public Kniha(string nazev) => _nazev = nazev;

    public string Nazev
    {
        get => _nazev;
        set
        {
            if (_nazev == value) return;
            _nazev = value;
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof(Nazev)));
        }
    }

    public event PropertyChangedEventHandler? PropertyChanged;
}
```

<details>
<summary>Očekávaný výstup a vysvětlení</summary>

```text
List[0]: Duna
Kolekce: Add
ID 1: Duna
ID 2 nenalezeno
Druhý zápis ID 1: False
Vlastnost: Nazev
Katalog po změně: Duna (opravený název)
Kolekce: Remove
```

`List` začíná indexem 0. `TryGetValue` pro neexistující ID vrátí `false`, takže program obslouží chybějící knihu bez výjimky. `TryAdd` odmítne druhý zápis stejného ID a původní knihu ponechá.

Přidání a odebrání vyvolají `CollectionChanged`. Změna názvu vyvolá pouze `PropertyChanged` na objektu knihy. Druhé přiřazení stejné hodnoty nic neoznámí díky podmínce v setteru. Katalog a seznam zde obsahují odkaz na tentýž objekt; proto se nový název objeví i při čtení přes slovník. Odebrání ze seznamu samo neodstraní položku ze slovníku.

</details>

Kód i uvedený výstup byly ověřeny 10. 9. 2026 kompilátorem ze SDK 10.0.400 a spuštěním na .NET 10.0.11. Ukázka je určená k ověření kolekcí a událostí v konzoli. Samotné navázání a aktualizaci ovládacích prvků WPF je potřeba ověřit zvlášť v tématu [datová vazba](@/psp/22-datova-vazba.md).

## Časté chyby

- Přístup `katalog[2]` by při chybějícím klíči vyvolal `KeyNotFoundException`; `TryGetValue` umožňuje tento stav běžně obsloužit.
- `TryAdd` vrací při duplicitě `false`. Přístup `katalog[1] = jinaKniha` by naopak položku slovníku nahradil; neaktualizoval by tím automaticky samostatný seznam.
- `ObservableCollection` nesleduje změny názvu uvnitř knihy. Je potřeba oznámení vlastnosti z objektu a příslušný odběratel události, například datová vazba.

## Otázky k procvičení

Kdy zvolit List a kdy Dictionary? Co musí oznamovat prvek navázané kolekce?

<details>
<summary>Kontrola odpovědi</summary>

`List` pro pořadí a průchod, `Dictionary` pro vyhledání podle klíče. Prvek musí oznamovat změny vlastností, typicky přes `INotifyPropertyChanged` a událost `PropertyChanged`; viz [příklad Microsoftu](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-implement-property-change-notification).

</details>

## Samostatný úkol

1. Změň vyhledávané ID z `2` na `1`. Před spuštěním předpověz, který řádek zmizí.
2. Za odebrání knihy přidej `Console.WriteLine(katalog.ContainsKey(1));`. Vysvětli výsledek a navrhni, kde by aplikace měla koordinovat odstranění z obou kolekcí.
3. Dočasně zakomentuj vyvolání `PropertyChanged?.Invoke(...)`. Hodnota názvu se stále změní, ale odběratel o ní nedostane zprávu. Porovnej výstup a potom oznámení obnov.

Ulož oba výstupy a vlastní vysvětlení. Než odkryješ kontrolu příkladu, označ události kolekce a události samotné knihy.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).

Chování metod a oznámení: Microsoft Learn — [TryGetValue](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2.trygetvalue?view=net-10.0), [TryAdd](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2.tryadd?view=net-10.0), [ObservableCollection](https://learn.microsoft.com/en-us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=net-10.0) a [oznámení změny vlastnosti](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-implement-property-change-notification).
