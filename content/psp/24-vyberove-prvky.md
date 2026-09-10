+++
title = "PSP 24 – Listbox, Combobox, Radiobutton, Checkbox"
description = "Listbox, Combobox, Radiobutton, Checkbox – výklad, praktický příklad a ověření znalostí."
date = 2026-09-09
weight = 24
[extra]
author = "Dany Chaker"
cislo = 24
subject = "psp"
status = "study"
+++

[← Seznam témat](@/posts/site-a-programovani.md)

## Co vysvětlit u zkoušky

ListBox zobrazuje seznam a podporuje výběr podle nastavení, ComboBox nabízí výběr v rozbalovacím seznamu. RadioButton tvoří skupinu vzájemně výlučných voleb, CheckBox nezávislou ano/ne volbu nebo případně třístavovou hodnotu. ItemsSource určuje data a SelectedItem vybraný objekt; zobrazení lze upravit šablonou. Index není trvalý identifikátor, protože se může změnit řazením. GroupName pomáhá jednoznačně vymezit skupinu přepínačů. Popisky musí vysvětlit význam voleb a klávesnice umožnit použití. Prázdný výběr je platný stav, který musí obsluha rozpoznat.

## Praktický příklad

Navrhni filtr knih: ComboBox pro kategorii, CheckBox pro pouze dostupné a ListBox pro výsledky. Vyber knihu, změň filtr tak, že zmizí, a ošetři zrušený výběr. Detaily zobrazuj podle objektu nebo stabilního ID.

## Časté chyby

Nepoužívej SelectedIndex jako ID v databázi. Přepínače se stejným významem musí patřit do stejné výlučné skupiny.

## Otázky k procvičení

Kdy použiješ checkbox a kdy radio button? Co když SelectedItem vrátí null?

<details>
<summary>Kontrola odpovědi</summary>

Checkbox pro nezávislou volbu, radio pro jednu z více možností. Obsluha nesmí dereferencovat null a má zobrazit stav bez výběru.

</details>

## Samostatný úkol

Zpracuj uvedený příklad bez čtení výkladu. Potom změň jeden vstup nebo podmínku a vysvětli, co se změní ve výsledku. Ulož výstup a připoj krátké zdůvodnění svého postupu.

## Zdroje a platnost

Číslování podle [školního PDF pro rok 2026](../../MZ-IT.pdf); použití témat pro rok 2027 čeká na potvrzení školy. [Odborné zdroje a doporučení k ověřování](@/posts/odborne-zdroje.md).
