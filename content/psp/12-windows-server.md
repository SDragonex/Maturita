+++
title = "PSP 12 – Operační systém Windows – servery"
description = "Operační systém Windows – servery – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 12
[extra]
author = "Dany Chaker"
cislo = 12
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Windows Server může poskytovat adresářové služby, DNS, DHCP, souborové sdílení a další role. Active Directory Domain Services spravuje doménové objekty a ověřování. Doména se liší od pracovní skupiny centrální správou účtů a politik. DNS je zásadní pro vyhledání doménových služeb. Organizační jednotky pomáhají uspořádat objekty a cílit Group Policy. Přístup ke sdíleným souborům ovlivňují oprávnění sdílení i souborového systému; při přístupu po síti musí vyhovět oběma. Správa zahrnuje logy, aktualizace, zálohy a obnovu konfigurace i dat.

## Praktický příklad

V laboratorní doméně vytvoř skupinu Studenti a sdílenou složku. Oprávnění přiřaď skupině, potom ověř přístup běžným uživatelem. Zkontroluj přihlášení, DNS a aplikaci politik; neměř úspěch pouze z administrátorského účtu.

## Časté chyby

Lokální účet není doménový účet se stejným jménem. Příliš široká oprávnění sdílení neopravují bezpečně chybu skupin.

## Otázky k procvičení

Proč dávat práva skupinám? Jak odlišíš lokální a doménové přihlášení?

<details>
<summary>Kontrola odpovědi</summary>

Skupiny zjednodušují jednotnou správu. Sleduj autoritu účtu, například název počítače nebo domény, ne pouze uživatelské jméno.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
