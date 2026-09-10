+++
title = "PSP 26 – Vektorová grafika v C#"
description = "Vektorová grafika v C# – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 26
[extra]
author = "Dany Chaker"
cislo = 26
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

Ve WPF tvoří vektorovou grafiku například Line, Rectangle, Ellipse, Polygon a Path. Shape je UI prvek s vlastnostmi Fill, Stroke a rozměry; Geometry popisuje tvar a Drawing může být lehčí pro větší množství kresby. Canvas umísťuje prvky souřadnicemi, jiné panely slouží pro běžný layout. Souřadnice se obvykle vyjadřují v jednotkách nezávislých na zařízení. Transformace zahrnují posun, rotaci a měřítko; pořadí jejich skládání ovlivňuje výsledek. RenderTransform mění vykreslení bez stejného přepočtu layoutu jako LayoutTransform. Hit testing zjišťuje zásah myší do prvku.

## Praktický příklad

V Canvas vytvoř obdélník a elipsu s různým Fill a Stroke. Umožni výběr a posun tvaru. Potom změň měřítko zobrazení a ověř souřadnice myši i šířku obrysu. Pro větší množství tvarů zvaž vhodnější kreslicí reprezentaci.

## Časté chyby

Zvětšení vektorového tvaru a bitmapy má jiné důsledky. Pevné souřadnice plátna neřeší automaticky responzivní formulář.

## Otázky k procvičení

Jak se liší Shape a Geometry? Proč záleží na pořadí posunu a rotace?

<details>
<summary>Kontrola odpovědi</summary>

Shape je UI prvek, Geometry popisuje geometrii. Transformace se skládají a obecně nejsou zaměnitelné.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
