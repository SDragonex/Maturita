+++
title = "PSP 5 – Technické prvky sítí, topologie LAN a WAN"
description = "Technické prvky sítí, topologie LAN a WAN – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 5
[extra]
author = "Dany Chaker"
cislo = 5
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Síťová karta připojuje zařízení k médiu. Repeater regeneruje signál, hub jej opakuje na více portů, switch rozhoduje podle linkové tabulky a router podle směrovací tabulky. Access point propojuje bezdrátové klienty se sítí, firewall prosazuje pravidla provozu. Fyzická topologie popisuje skutečné kabely a zařízení, logická tok komunikace. Hvězda zjednodušuje správu, ale centrální prvek může být bodem selhání. Mesh nabízí alternativní cesty za cenu složitosti. Redundance má smysl jen s mechanismem, který zabrání smyčkám a ověří přepnutí.

## Praktický příklad

Nakresli kancelář s centrálním switchem, AP a routerem do internetu. Označ dopad výpadku každé části. Potom navrhni záložní internetové spojení a uveď, jak bude síť detekovat závadu a přepínat.

## Časté chyby

Domácí krabička může spojovat router, switch, AP i firewall. Název jednoho zařízení neznamená, že dělá jen jednu funkci.

## Otázky k procvičení

Jak se liší switch a hub? Je druhý kabel automaticky funkční záloha?

<details>
<summary>Kontrola odpovědi</summary>

Switch vybírá výstupní port podle cíle, hub opakuje signál. Druhý kabel vyžaduje správný návrh smyček/agregace a test přepnutí.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
