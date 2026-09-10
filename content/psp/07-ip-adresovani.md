+++
title = "PSP 7 – Adresování v TCP/IP sítích"
description = "Adresování v TCP/IP sítích – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 7
[extra]
author = "Dany Chaker"
cislo = 7
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

IPv4 má 32 bitů; prefix CIDR určuje počet síťových bitů a zbývající bity část hostitele. Maska odděluje síť od hostitele. V běžné podsíti se adresa s nulovými hostitelskými bity používá pro síť a s jedničkovými pro broadcast. Pravidlo minus dvě má výjimky, například spoje /31 a adresy /32. Soukromé rozsahy IPv4 se globálně nesměrují jako veřejné adresy. IPv6 má 128 bitů, používá prefixy a neobsahuje broadcast jako IPv4; příslušné funkce řeší mimo jiné multicast. Výchozí brána je další uzel pro cíle mimo místní síť. DNS server překládá názvy, není to nutně brána.

## Praktický příklad

Pro 192.168.10.70/26 je maska 255.255.255.192. Blok má 64 adres: síť 192.168.10.64, broadcast .127, běžní hostitelé .65 až .126, celkem 62. Adresa .130 je mimo tuto podsíť. V IPv6 zkracuj běh nul pomocí dvojité dvojtečky nejvýše jednou.

## Časté chyby

Neurčuj síť jen podle prvních tří čísel. Například 192.168.10.70/26 a 192.168.10.130/26 mají stejné první tři oktety, ale první patří do 192.168.10.64/26 a druhá do 192.168.10.128/26. Stejná délka prefixu `/26` neznamená stejný síťový prefix. Pravidlo odečtení dvou adres nepoužívej bezmyšlenkovitě: na spoji bod–bod s `/31` se obě adresy používají pro koncová rozhraní, viz [RFC 3021, oddíl 2.1](https://www.rfc-editor.org/rfc/rfc3021#section-2.1).

## Otázky k procvičení

Rozděl /24 na čtyři stejné podsítě. Kolik běžných hostitelů má každá?

<details>
<summary>Kontrola odpovědi</summary>

Vzniknou čtyři /26 s počátky .0, .64, .128 a .192. Každá má 64 adres a obvykle 62 hostitelů.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
