+++
title = "PSP 9 – Router"
description = "Router – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 9
[extra]
author = "Dany Chaker"
cislo = 9
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Router propojuje IP sítě a pro každý paket rozhoduje o dalším skoku nebo výstupním rozhraní. Rozhraní mají vlastní adresaci; přímo připojené sítě tvoří část směrovací tabulky. Paket se při předání zabalí do nového linkového rámce a snižuje se TTL nebo hop limit. Router může současně poskytovat DHCP, NAT a firewall, ale tyto funkce nejsou samotným směrováním. NAT přepisuje adresy a případně porty; sám není úplnou bezpečnostní politikou. Správa vyžaduje řízený přístup, zálohu konfigurace a dokumentaci změn.

## Praktický příklad

Propoj LAN 192.168.1.0/24 a 192.168.2.0/24 rozhraními .1. Hostům nastav odpovídající bránu. Ověř místní spojení, dosažitelnost brány a následně vzdálenou síť. Přidej pravidlo, které dovolí jen požadovanou službu, a otestuj i zamítnutí.

## Časté chyby

Pravidlo firewallu může blokovat ping a přitom povolit web. Samotný neúspěšný ping není důkaz výpadku všech služeb.

## Otázky k procvičení

Co se na routeru stane s Ethernetovým rámcem? Kde hledáš chybu, když funguje brána, ale ne vzdálený host?

<details>
<summary>Kontrola odpovědi</summary>

Původní rámec se zpracuje a pro další linku vznikne nový. Zkontroluj trasy, zpáteční cestu, pravidla a cílovou službu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
