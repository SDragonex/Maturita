+++
title = "ASW 17 – Bezpečnost a zálohování"
description = "Bezpečnost a zálohování – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 17
[extra]
author = "Dany Chaker"
cislo = 17
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Bezpečnost zahrnuje důvěrnost, integritu a dostupnost dat. Hrozba je možná příčina škody, zranitelnost slabé místo a riziko spojuje pravděpodobnost s dopadem. Ochranu tvoří aktualizace, silné unikátní přihlašování, vícefaktorové ověření, přiměřená oprávnění a kontrola vstupů. Phishing zneužívá důvěru; rozhoduje ověření požadavku a domény, nikoli jen vzhled zprávy. Záloha slouží k obnově po omylu, poruše či napadení. Synchronizace může rozšířit i smazání. Oddělené kopie a verze omezují společný bod selhání. Obnova musí být skutečně odzkoušena.

## Praktický příklad

Pro maturitní projekt uchovávej pracovní kopii, verzovaný repozitář a oddělenou zálohu příloh. Do prázdné složky obnov projekt a sestav jej podle návodu. Změř, o kolik práce bys přišel a jak dlouho obnova trvá.

## Časté chyby

Antivirus není záruka a RAID nenahrazuje zálohu. Nezapisuj hesla a klíče do veřejného repozitáře.

## Otázky k procvičení

Proč synchronizace není vždy záloha? Jak poznáš použitelnou zálohu?

<details>
<summary>Kontrola odpovědi</summary>

Může přenést smazání nebo poškození. Použitelnost doloží úspěšná obnova potřebných dat a funkční spuštění.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
