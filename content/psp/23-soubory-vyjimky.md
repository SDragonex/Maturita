+++
title = "PSP 23 – Soubory, výjimky"
description = "Soubory, výjimky – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 23
[extra]
author = "Dany Chaker"
cislo = 23
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Práce se soubory zahrnuje cesty, kódování, otevření, čtení, zápis a uvolnění prostředků. Relativní cesta závisí na pracovním adresáři, ne nutně na umístění programu. Pomocí Path.Combine skládej části cesty, ale ověř i zamýšlené místo a povolené vstupy. Using zajistí uvolnění IDisposable prostředku. Výjimka přeruší běžný tok; catch má řešit očekávaný problém a finally úklid. Chybu nepolykej bez informace. Ukládání musí počítat s chybějícími právy, plným diskem a poškozeným souborem. Pro důležitá data je vhodné zapisovat novou verzi a teprve po úspěchu ji předat jako finální.

## Praktický příklad

Navrhni uložení seznamu úkolů do JSON. Nejdřív serializuj a zapiš do dočasného souboru ve stejné složce; potom použij vhodnou operaci nahrazení podle platformy. Otestuj načtení chybného JSON a nemožnost zápisu tak, aby stará data zůstala použitelná.

## Časté chyby

Existence souboru před operací nezaručuje, že bude dostupný o chvíli později. Catch Exception bez řešení může zakrýt skutečný problém.

## Otázky k procvičení

Proč using? Co má uživatel vidět po neúspěšném uložení?

<details>
<summary>Kontrola odpovědi</summary>

Uvolní prostředek i při výjimce. Jasnou chybu a zachovaná data; aplikace nesmí tvrdit, že změny uložila.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
