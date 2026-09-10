+++
title = "ASW 24 – Dynamické webové stránky"
description = "Dynamické webové stránky – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 24
[extra]
author = "Dany Chaker"
cislo = 24
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Dynamický web mění obsah podle dat nebo interakce. Klient zpracovává rozhraní a události, server ověřuje požadavky, oprávnění a pracuje s uloženými daty. HTTP požadavek má metodu, adresu, hlavičky a případně tělo; odpověď má stav a obsah. Asynchronní požadavek může uspět, selhat nebo trvat dlouho, takže UI potřebuje všechny tyto stavy. Validace v prohlížeči pomáhá uživateli, validace na serveru chrání data. Autentizace zjišťuje identitu, autorizace povoluje konkrétní operaci. Citlivá tajemství nepatří do kódu staženého prohlížečem.

## Praktický příklad

Navrhni seznam úkolů: načtení, přidání a označení hotového. Uveď pro každou akci požadavek a očekávanou odpověď. Při chybě uložení zachovej text formuláře a umožni opakování. Na serveru kontroluj, že uživatel upravuje svůj úkol.

## Časté chyby

Úspěšný HTTP přenos nemusí znamenat platný výsledek aplikace. Nikdy neskládej SQL dotaz prostým připojením uživatelského vstupu.

## Otázky k procvičení

Proč nestačí skrýt tlačítko Smazat? Jaký stav UI ukážeš při pomalém připojení?

<details>
<summary>Kontrola odpovědi</summary>

Požadavek lze poslat i mimo UI, oprávnění musí kontrolovat server. Zobraz průběh a zabraň nechtěnému opakovanému odeslání.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
