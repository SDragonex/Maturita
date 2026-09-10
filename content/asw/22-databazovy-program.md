+++
title = "ASW 22 – Práce v databázovém programu"
description = "Práce v databázovém programu – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 22
[extra]
author = "Dany Chaker"
cislo = 22
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Databázový program umožňuje vytvářet tabulky, dotazy, formuláře a sestavy. Tabulka ukládá záznamy s určenými typy polí, primární klíč jednoznačně identifikuje řádek a cizí klíč propojuje tabulky. Formulář usnadňuje zadání dat; pravidla integrity však mají chránit data i mimo něj. Dotaz vybírá a spojuje údaje, sestava je formátuje pro čtení nebo tisk. Import vyžaduje kontrolu typů, znakové sady a duplicit. Databázový soubor a aplikace nejsou totéž; při více uživatelích je nutné řešit souběh a oprávnění.

## Praktický příklad

Vytvoř tabulky Student a Vypujcka propojené studentovým ID. Ve formuláři vybírej studenta z nabídky, dotazem zobraz nevrácené knihy a sestavou vytvoř přehled. Ověř, že nelze založit výpůjčku neexistujícímu studentovi.

## Časté chyby

Jméno člověka není vhodný jednoznačný identifikátor. Kopírování celých údajů studenta do každé výpůjčky vytváří rozpory.

## Otázky k procvičení

Čím se liší dotaz a sestava? Proč potřebuješ cizí klíč i při výběru z formuláře?

<details>
<summary>Kontrola odpovědi</summary>

Dotaz určuje data, sestava jejich výstupní podobu. Cizí klíč chrání vazbu i při importu či přímém zápisu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
