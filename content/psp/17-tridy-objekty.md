+++
title = "PSP 17 – Objektově orientovaný přístup, třídy, metody, atributy, konstruktor"
description = "Objektově orientovaný přístup, třídy, metody, atributy, konstruktor – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 17
[extra]
author = "Dany Chaker"
cislo = 17
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Třída definuje stav a chování, objekt je její instance. Pole ukládá stav, vlastnost poskytuje řízený přístup a metoda provádí operaci. Konstruktor připravuje platný počáteční stav. Přístupové modifikátory určují viditelnost členů. Zapouzdření znamená udržovat pravidla objektu, nikoli jen napsat private. Parametry metod předávají vstupy a návratová hodnota výstup. Rozliš školní obecné označení atribut jako vlastnost objektu od C# attributes, která představují metadata v hranatých závorkách. Instance jedné třídy mohou mít odlišné hodnoty.

## Praktický příklad

Navrhni Trida Ucet s privátním zůstatkem, veřejným čtením a metodou Vloz. Konstruktor a metoda nesmějí přijmout zápornou částku, pokud ji model zakazuje. Vytvoř dva objekty a ověř, že vklad do jednoho nemění druhý.

## Časté chyby

Veřejná měnitelná pole mohou obejít pravidla. Konstruktor nemá návratový typ a nezaměňuje se s běžnou metodou.

## Otázky k procvičení

Proč chránit změnu zůstatku metodou? Jak se liší třída a instance?

<details>
<summary>Kontrola odpovědi</summary>

Metoda může ověřit pravidla před změnou. Třída popisuje typ, instance konkrétní stav v paměti.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
