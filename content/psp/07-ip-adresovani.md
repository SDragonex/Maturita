+++
title = "PSP 7 – Adresování v TCP/IP sítích"
description = "Adresování v TCP/IP sítích – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
updated = 2026-09-10
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

Počítač A má adresu **192.168.10.70/26**, počítač B **192.168.10.130/26**. Urči jejich podsítě, rozsahy adres hostitelů a rozhodni, zda patří do stejné IP podsítě. Předpokládej běžné IPv4 podsítě s touto maskou.

### 1. Od prefixu k masce a velikosti bloku

Prefix `/26` vyhrazuje síti 26 z 32 bitů. Pro hostitele zbývá `32 − 26 = 6` bitů. Maska má 26 jedniček a za nimi šest nul:

```text
11111111.11111111.11111111.11000000 = 255.255.255.192
```

Poslední oktet masky je `128 + 64 = 192`. Celý blok má `2^6 = 64` adres, takže v rámci `192.168.10.0/24` začínají bloky na `.0`, `.64`, `.128` a `.192`. Význam délky prefixu a velikosti bloků popisuje [RFC 4632, oddíl 3.1](https://www.rfc-editor.org/rfc/rfc4632#section-3.1).

### 2. Určení síťové adresy

Síťovou adresu získáme bitovým AND adresy a masky: hostitelské bity se vynulují. První tři oktety zůstanou stejné, protože jejich maska je `255`. Poslední oktet vyjde takto:

```text
A:  01000110  (70)      B:  10000010  (130)
AND 11000000  (192)     AND 11000000  (192)
  = 01000000  (64)        = 10000000  (128)
```

Adresa `.70` tedy leží v bloku `.64–.127`, zatímco `.130` v bloku `.128–.191`. Broadcast je poslední adresa bloku; při jeho výpočtu nastavíme všech šest hostitelských bitů na jedničky.

### 3. Výsledek a jeho význam

| Údaj | Počítač A | Počítač B |
|---|---|---|
| Adresa rozhraní | `192.168.10.70/26` | `192.168.10.130/26` |
| Maska | `255.255.255.192` | `255.255.255.192` |
| Síť | `192.168.10.64/26` | `192.168.10.128/26` |
| Broadcast | `192.168.10.127` | `192.168.10.191` |
| První adresa hostitele | `192.168.10.65` | `192.168.10.129` |
| Poslední adresa hostitele | `192.168.10.126` | `192.168.10.190` |
| Všech adres / adres hostitelů | 64 / 62 | 64 / 62 |

V každé z těchto dvou podsítí odečteme síťovou adresu a broadcast: `64 − 2 = 62` adres hostitelů. Jde o kapacitu adresování, ne o počet právě připojených počítačů; adresu hostitele může používat také rozhraní směrovače.

**A a B patří do různých podsítí.** Rozhodují jejich síťové bity, nikoli podobnost desetinného zápisu. Dokonce číselně sousední `.127` a `.128` leží každý v jiném bloku; zde jde navíc o broadcast prvního bloku a síťovou adresu druhého, takže je nelze přiřadit běžným hostitelům. Nejbližší použitelné adresy po obou stranách této hranice jsou `.126` a `.129`.

<details>
<summary>Ověření výpočtu v Pythonu</summary>

Kód používá standardní knihovnu `ipaddress`. Ulož jej například jako `overeni_podsiti.py` a ve Windows spusť `py -3 overeni_podsiti.py`.

```python
from ipaddress import ip_interface

for address in ("192.168.10.70/26", "192.168.10.130/26"):
    network = ip_interface(address).network
    hosts = list(network.hosts())
    print(address, "->", network, network.netmask)
    print("broadcast:", network.broadcast_address)
    print("hosts:", hosts[0], "-", hosts[-1], "count:", len(hosts))
```

Ověřený výstup v Pythonu 3.14.5:

```text
192.168.10.70/26 -> 192.168.10.64/26 255.255.255.192
broadcast: 192.168.10.127
hosts: 192.168.10.65 - 192.168.10.126 count: 62
192.168.10.130/26 -> 192.168.10.128/26 255.255.255.192
broadcast: 192.168.10.191
hosts: 192.168.10.129 - 192.168.10.190 count: 62
```

`ip_interface` přijímá adresu rozhraní včetně prefixu; jeho vlastnost `network` vrací odpovídající síť. Metoda `hosts()` u těchto `/26` vynechá síťovou adresu a broadcast. Podrobnosti uvádí [dokumentace Pythonu](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hosts). Výpočet ověřuje adresní rozsahy, ne skutečnou konektivitu zařízení.

</details>

## Časté chyby

Stejná délka prefixu `/26` znamená stejně velké bloky, nikoli stejný síťový prefix. Síťová adresa se počítá z celé adresy a masky; samotné první tři oktety nestačí.

Pravidlo odečtení dvou adres nepoužívej bezmyšlenkovitě: **na spoji bod–bod s `/31` se obě adresy používají pro koncová rozhraní**. Například `192.0.2.0/31` má koncové adresy `192.0.2.0` a `192.0.2.1`; není v něm samostatná adresa pro směrovaný broadcast do této podsítě. Nejde o obecné doporučení pro běžnou síť s více uzly, viz [RFC 3021, oddíly 2.1 a 2.2](https://www.rfc-editor.org/rfc/rfc3021#section-2.1). Prefix `/32` označuje jedinou adresu, takže ani tam nevychází počet hostitelů jako „jedna minus dvě“.

V IPv6 zkracuj běh nul pomocí dvojité dvojtečky nejvýše jednou. Pravidla pro IPv4 broadcast nepřenášej do IPv6.

## Otázky k procvičení

Rozděl `192.168.10.0/24` na čtyři stejné podsítě. Kolik běžných hostitelů má každá a proč se délka prefixu změní o dva bity?

<details>
<summary>Kontrola odpovědi</summary>

Pro čtyři možnosti potřebujeme dva bity, protože `2^2 = 4`; prefix prodloužíme z `/24` na `/26`. Vzniknou `192.168.10.0/26`, `192.168.10.64/26`, `192.168.10.128/26` a `192.168.10.192/26`. Každá obsahuje 64 adres, z nichž 62 lze použít pro hostitele běžné podsítě.

</details>

## Samostatný úkol

Bez otevírání kontroly vyřeš dvojici **192.168.10.190/26** a **192.168.10.194/26**:

1. Pro obě adresy napiš masku, síť, broadcast, první a poslední adresu hostitele a počet adres hostitelů.
2. Rozhodni, zda jsou ve stejné podsíti. Vysvětli hranici mezi bloky a význam adres `.191` a `.192`.
3. Potom změň u obou prefix na `/24`. Přepočítej síť a rozsah hostitelů a vysvětli, proč se výsledek změnil.
4. Teprve nakonec porovnej výpočet s kontrolou nebo uprav vstupy v Pythonu výše. Ulož tabulku a vlastní zdůvodnění.

<details>
<summary>Kontrola samostatného úkolu</summary>

| Vstup | Síť | Broadcast | Hostitelé | Počet adres hostitelů |
|---|---|---|---|---:|
| `192.168.10.190/26` | `192.168.10.128/26` | `192.168.10.191` | `192.168.10.129–192.168.10.190` | 62 |
| `192.168.10.194/26` | `192.168.10.192/26` | `192.168.10.255` | `192.168.10.193–192.168.10.254` | 62 |

Obě masky jsou `255.255.255.192`. Adresy jsou v různých `/26`; `.191` je broadcast předchozího bloku a `.192` síťová adresa následujícího.

Při změně obou prefixů na `/24` je maska `255.255.255.0` a obě adresy patří do `192.168.10.0/24`. Broadcast je `192.168.10.255`, hostitelé `192.168.10.1–192.168.10.254`, celkem 254 adres. Pro hostitele zbývá osm bitů místo šesti, takže poslední oktet už nerozlišuje čtyři různé podsítě. Jde o změnu zadání výpočtu, nikoli pokyn měnit konfiguraci skutečné školní sítě.

</details>

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
