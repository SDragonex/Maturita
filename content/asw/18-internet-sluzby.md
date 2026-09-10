+++
title = "ASW 18 – Internet a jeho služby"
description = "Internet a jeho služby – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 18
[extra]
author = "Dany Chaker"
cislo = 18
subject = "asw"
status = "study"
+++

[← Seznam témat](@/posts/aplikacni-software.md)

## Co vysvětlit u zkoušky

Internet propojuje sítě pomocí IP. Web používá HTTP/HTTPS, pošta například SMTP a IMAP a DNS překládá doménová jména na příslušné záznamy. URL obsahuje schéma, hostitele a případně port, cestu, dotaz a fragment. Prohlížeč zpracuje odpověď a načte další zdroje. HTTPS chrání přenos a ověřuje server certifikátem, ale samo nezaručuje pravdivost obsahu. Klient žádá službu, server ji poskytuje; stejný stroj může zastávat obě role. Cache zrychluje opakované použití, ale komplikuje okamžité zobrazení změn. Soukromá adresa není automaticky dostupná z internetu.

## Praktický příklad

Popiš otevření https://example.org/lekce?q=site#uvod: schéma https, host example.org, cesta /lekce, dotaz q=site, fragment uvod. Fragment běžný prohlížeč neposílá serveru jako součást HTTP požadavku.

## Časté chyby

Web není celý internet. Ikona zabezpečeného připojení neznamená, že obchod nebo informace jsou důvěryhodné.

## Otázky k procvičení

Jak odlišíš problém DNS od chyby webové aplikace? K čemu slouží cache?

<details>
<summary>Kontrola odpovědi</summary>

DNS problém brání nalezení adresy; aplikace může vrátit HTTP chybu až po spojení. Cache uchovává dřívější výsledky pro další použití.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
