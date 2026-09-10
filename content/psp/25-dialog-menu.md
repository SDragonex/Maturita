+++
title = "PSP 25 – MessageBox, vlastní dialogové okno, Menu"
description = "MessageBox, vlastní dialogové okno, Menu – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 25
[extra]
author = "Dany Chaker"
cislo = 25
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

MessageBox slouží pro krátkou zprávu nebo rozhodnutí, vlastní dialog pro složitější vstup. Modální okno blokuje interakci s vlastníkem, nemodální umožňuje souběžnou práci. Owner určuje vztah k rodiči a pomáhá chování oken. ShowDialog vrací nullable bool; zavření křížkem nemusí znamenat souhlas. Menu sdružuje akce, příkazy a klávesové zkratky. Stav CanExecute může deaktivovat nedostupnou akci. U změn dat rozliš potvrzení, zrušení a pokračování v práci. Dialog má jasně popsat důsledek a neztratit vstup při chybě.

## Praktický příklad

Při zavírání neuloženého dokumentu nabídni Uložit, Zahodit změny a Zrušit. Pokud uživatel zruší výběr souboru nebo zápis selže, okno zůstane otevřené. Ověř menu Zavřít i křížek okna.

## Časté chyby

Zavření dialogu křížkem nesmí samo potvrdit destruktivní operaci. Dialog bez vlastníka se může schovat za hlavní okno.

## Otázky k procvičení

Proč nestačí kontrola jen tlačítka Zavřít? Co se stane při zrušení ukládání?

<details>
<summary>Kontrola odpovědi</summary>

Okno lze zavřít i jinými cestami. Zrušení ukládání má zastavit navazující zavření a zachovat pracovní stav.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
