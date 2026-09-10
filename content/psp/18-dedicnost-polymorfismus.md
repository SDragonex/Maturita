+++
title = "PSP 18 – Dědičnost, polymorfismus, zapouzdření, statické metody a třídy"
description = "Dědičnost, polymorfismus, zapouzdření, statické metody a třídy – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 18
[extra]
author = "Dany Chaker"
cislo = 18
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Dědičnost vyjadřuje vztah je typem a umožňuje odvodit třídu ze základní. Kompozice skládá objekt z jiných objektů a bývá vhodná pro vztah má. Polymorfismus dovoluje volat společné rozhraní s různým konkrétním chováním. Virtual člen lze přepsat pomocí override; abstract požaduje implementaci v neabstraktní odvozené třídě. Interface definuje smlouvu. Static člen patří typu, nikoli jednotlivé instanci; nemá přístup k instančnímu stavu bez objektu. Zapouzdření chrání vnitřní invarianty. Přetížení metody podle parametrů není totéž co přepsání v odvozené třídě.

## Praktický příklad

Vytvoř rozhraní ITvar s metodou Obsah a dvě implementace Kruh a Obdelnik. Projdi kolekci ITvar a vypiš obsah bez testování konkrétního typu. Výpočet každého tvaru musí používat vlastní rozměry a ověřovat platný vstup.

## Časté chyby

Použití new pro skrytí metody nenahrazuje override. Globální statický stav může nechtěně propojit nezávislé části programu.

## Otázky k procvičení

Kdy dát přednost kompozici? Je přetížení totéž co polymorfní přepsání?

<details>
<summary>Kontrola odpovědi</summary>

Když objekt používá jiný objekt, ale není jeho druhem. Přetížení rozlišuje podpisy metod; override mění chování zděděného virtuálního členu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
