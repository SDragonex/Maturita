+++
title = "ASW 25 – Návrh databází"
description = "Návrh databází – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 25
[extra]
author = "Dany Chaker"
cislo = 25
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Návrh databáze vychází z entit, vztahů a pravidel použití. Entita má atributy; klíč jednoznačně identifikuje záznam. Vztah 1:N zpravidla reprezentuje cizí klíč na straně N, vztah M:N spojovací tabulka. Normalizace omezuje redundanci a aktualizační anomálie. V 1NF mají pole atomické hodnoty v rámci zvoleného modelu, ve 2NF nejsou neklíčové atributy závislé jen na části kandidátního složeného klíče a ve 3NF se odstraňují nevhodné tranzitivní závislosti. Omezení NOT NULL, UNIQUE a cizí klíče vynucují pravidla. Transakce seskupuje změny do ucelené operace.

## Praktický příklad

Studenti navštěvují více kurzů a kurz má více studentů. Navrhni Student(id, jmeno), Kurz(id, nazev) a Zapis(student_id, kurz_id). Dvojice ve spojovací tabulce musí být jedinečná. Zvaž, kam patří datum zápisu: popisuje vztah, proto do Zapis.

## Časté chyby

Seznam ID oddělený čárkami v jednom poli komplikuje integritu i dotazy. Nadbytečný index zpomaluje zápisy a zabírá místo.

## Otázky k procvičení

Jak uložíš vztah M:N? Proč má bankovní převod tvořit jednu transakci?

<details>
<summary>Kontrola odpovědi</summary>

Spojovací tabulkou se dvěma vazbami. Odečtení i přičtení se musí provést společně, nebo obě změny vrátit.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
