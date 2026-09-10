+++
title = "PSP 3 – Architektura ISO/OSI modelu a TCP/IP"
description = "Architektura ISO/OSI modelu a TCP/IP – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 3
[extra]
author = "Dany Chaker"
cislo = 3
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Referenční model OSI má vrstvy fyzickou, linkovou, síťovou, transportní, relační, prezentační a aplikační. TCP/IP se běžně popisuje vrstvami přístupu k síti, internetovou, transportní a aplikační; mapování není přesně jedna ku jedné. Zapouzdření přidává informace potřebné jednotlivými vrstvami. Ethernet používá rámce a MAC adresy, IP pakety a IP adresy, TCP/UDP porty. TCP poskytuje uspořádaný proud s potvrzováním a opakováním přenosu; UDP datagramy bez těchto záruk. Spolehlivost aplikace však závisí i na jejím návrhu, nikoli jen na volbě transportu.

## Praktický příklad

Popiš odeslání požadavku přes HTTPS: aplikační data, zabezpečený přenos, transport, IP a linka. Pro jednoduchý model HTTP přes TCP sleduj port serveru 443 a změnu linkových adres při průchodu routerem. Upozorni, že HTTP/3 používá QUIC nad UDP.

## Časté chyby

Nezaměňuj segment, paket a rámec. UDP automaticky neznamená chybné nebo nezabezpečené spojení.

## Otázky k procvičení

Proč se linkové adresy mění na routeru? K čemu jsou porty?

<details>
<summary>Kontrola odpovědi</summary>

Každý další linkový úsek má vlastní rámec. Porty rozlišují komunikační koncové body služeb/aplikací v rámci hostitele.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
