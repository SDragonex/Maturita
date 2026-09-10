+++
title = "PSP 6 – Standardy síťového hardware – Ethernet, bezdrátové sítě"
description = "Standardy síťového hardware – Ethernet, bezdrátové sítě – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 6
[extra]
author = "Dany Chaker"
cislo = 6
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Ethernet je rodina standardů IEEE 802.3, WLAN se opírá o IEEE 802.11. Označení variant popisují různé rychlosti, média a další vlastnosti; kompatibilitu je nutné ověřit na obou koncích. MAC adresa identifikuje linkové rozhraní, ne trvale konkrétního člověka. Wi-Fi sdílí rádiové prostředí a její výkon ovlivňují vzdálenost, překážky, kanály a počet klientů. Šířka kanálu může zvýšit kapacitu, ale i nároky na volné spektrum. SSID je jméno sítě; jeho skrytí není spolehlivá ochrana. Zabezpečení nastav podle podporovaných aktuálních možností a potřeb organizace.

## Praktický příklad

V učebně změř rychlost po kabelu a přes Wi-Fi na stejný místní server, aby výsledek neomezoval internet. Potom zopakuj test dál od AP a s více aktivními klienty. Zaznamenej podmínky, ne pouze nejvyšší číslo.

## Časté chyby

Marketingová PHY rychlost není aplikační propustnost. Stejné SSID neznamená stejnou bezpečnost ani stejného provozovatele.

## Otázky k procvičení

Proč se mění výkon Wi-Fi při přesunu? Co oddělí místní test od internetového?

<details>
<summary>Kontrola odpovědi</summary>

Mění se kvalita signálu, rušení a zvolená modulace. Místní server pomůže odlišit problém WLAN od poskytovatele internetu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
