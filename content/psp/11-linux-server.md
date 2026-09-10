+++
title = "PSP 11 – Operační systém Linux – servery"
description = "Operační systém Linux – servery – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 11
[extra]
author = "Dany Chaker"
cislo = 11
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Linuxový server se spravuje přes účty, oprávnění, balíčky, služby, síť a logy. Kořen souborového systému je lomítko; konfigurační a datové adresáře mají odlišný účel. Práva vlastníka, skupiny a ostatních rozlišují čtení, zápis a spuštění; u adresáře spuštění dovoluje průchod. V distribucích se systemd slouží systemctl pro správu služeb a journalctl pro záznamy. Síť ověřuj od rozhraní přes adresy a trasy až po naslouchající službu. Změny konfigurace nejprve zálohuj a po úpravě ověř jejich syntaxi. Vzdálenou správu neprováděj tak, že se neotestovaným pravidlem odřízneš.

## Praktický příklad

Na laboratorním stroji zjisti adresy pomocí ip address, trasy pomocí ip route a naslouchající sockety pomocí ss -lnt. U konkrétní služby zkontroluj stav a log. Pokud běží lokálně, ale není dostupná ze sítě, prověř bind adresu a firewall.

## Časté chyby

Neřeš každý problém právy 777. Příkazy pro balíčky se mezi distribucemi liší a nelze je slepě zaměňovat.

## Otázky k procvičení

Proč běžící proces nemusí znamenat dostupnou službu? Co dělá právo x na adresáři?

<details>
<summary>Kontrola odpovědi</summary>

Proces nemusí naslouchat na správném rozhraní nebo ho blokují pravidla. Právo x dovoluje průchod a přístup k položkám při znalosti jejich názvu.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
