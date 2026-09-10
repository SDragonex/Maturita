+++
title = "PSP 10 – EtherChannel"
description = "EtherChannel – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 10
[extra]
author = "Dany Chaker"
cislo = 10
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

EtherChannel je označení agregace více fyzických ethernetových spojů do jednoho logického. Přináší vyšší souhrnnou kapacitu a redundanci. Pro vyjednávání lze použít LACP; statická agregace vyžaduje shodný ruční návrh. Členské porty musejí mít kompatibilní konfiguraci, například rychlost a režim VLAN. Rozdělování provozu obvykle používá hash z adres nebo portů, takže jeden tok zpravidla nevyužije součet rychlostí všech kabelů. Logické spojení se má správně promítnout do STP. Konkrétní příkazy a dostupné režimy se liší podle zařízení a systému.

## Praktický příklad

Dva gigabitové spoje agreguj mezi přepínači v laboratorním prostředí. Ověř členství portů, stav LACP a povolené VLAN. Změř jeden tok i více různých toků a následně odpoj jeden členský kabel. Sleduj přerušení a dostupnou kapacitu.

## Časté chyby

Čtyři linky po 1 Gb/s nezaručují jednomu přenosu 4 Gb/s. Nespojuj porty bez shodné konfigurace na protější straně. U LACP alespoň jedna strana vyjednávání musí být v režimu `active`; dvojice `passive`–`passive` jej nezahájí. Režim statického spojení `on` LACP nepoužívá. Ověř tyto režimy v [konfigurační příručce Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/etherchannel/etherchannel-configuration-guide/etherchannels.html).

## Otázky k procvičení

K čemu slouží LACP? Proč se více toků může rozložit lépe než jeden?

<details>
<summary>Kontrola odpovědi</summary>

Vyjednává a kontroluje členství v agregaci. Hash může odlišné toky přiřadit různým fyzickým linkám.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
