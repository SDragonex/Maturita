+++
title = "PSP 2 – Sítě LAN – charakteristika"
description = "Sítě LAN – charakteristika – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 2
[extra]
author = "Dany Chaker"
cislo = 2
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

LAN tvoří koncová zařízení, přepínače, přenosová média a případně bezdrátové přístupové body. Switch se učí zdrojové MAC adresy a používá tabulku k předání rámce. Neznámý unicast a broadcast obvykle rozesílá do příslušné VLAN mimo vstupní port. VLAN odděluje logické broadcastové domény; komunikace mezi nimi vyžaduje směrování. Full-duplex spojení mezi přepínačem a zařízením odstraňuje kolize typické pro starší sdílený Ethernet. Smyčky na druhé vrstvě mohou množit rámce; STP vytváří bezsmyčkovou aktivní topologii. Dokumentace LAN obsahuje porty, VLAN, adresaci a účel segmentů.

## Praktický příklad

Navrhni VLAN pro studenty a správu. Dva počítače v jedné VLAN mají komunikovat přímo, přístup do správy musí procházet řízeným směrováním. Vyzkoušej známý i neznámý cíl a sleduj MAC tabulku přepínače.

## Časté chyby

Stejná IP podsíť automaticky nepřeklene dvě oddělené VLAN. Připojení druhého kabelu bez řízení smyček může síť vyřadit.

## Otázky k procvičení

Kdy switch rozesílá rámec více porty? Proč VLAN sama neřeší všechna oprávnění?

<details>
<summary>Kontrola odpovědi</summary>

Například u broadcastu nebo neznámého cíle uvnitř VLAN. Pravidla mezi segmenty musí vynucovat směrování, ACL nebo firewall.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
