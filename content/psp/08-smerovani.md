+++
title = "PSP 8 – Směrování a směrovací protokoly"
description = "Směrování a směrovací protokoly – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 8
[extra]
author = "Dany Chaker"
cislo = 8
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Router vybere trasu podle cílové IP adresy. Nejprve hledá nejdelší odpovídající prefix; výchozí trasa /0 se použije, pokud chybí přesnější. Statické trasy nastavuje správce, dynamické směrovací protokoly si předávají informace. RIP je distance-vector protokol s metrikou počtu skoků, OSPF link-state protokol s výpočtem cest a BGP slouží zejména ke směrování mezi autonomními systémy podle politik. Metrika a důvěryhodnost zdroje trasy mají rozdílné role. Konvergence je ustálení směrování po změně. Funkční komunikace vyžaduje i zpáteční cestu.

## Praktický příklad

Tabulka obsahuje 10.0.0.0/8 přes A, 10.2.0.0/16 přes B a 0.0.0.0/0 přes C. Pro 10.2.3.4 se vybere B, pro 10.9.1.1 A a pro veřejný cíl C. Potom přidej výpadek B a popiš, co skutečně určí náhradní trasu.

## Časté chyby

Nezaměňuj směrování s NAT. Nejmenší metrika neporazí přesnější prefix pouze tím, že je číselně menší.

## Otázky k procvičení

Která trasa vyhraje pro cíl odpovídající /16 i /24? Proč potřebuješ zpáteční trasu?

<details>
<summary>Kontrola odpovědi</summary>

Přesnější /24. Odpověď musí umět najít cestu zpět, jinak samotné doručení požadavku nestačí.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
