# Protokol ověření

Kontroly proběhly **9.–10. 9. 2026** na Windows v místním pracovním stromu. Web se připravuje pro jaro a podzim 2027. Technická kontrola a věcná revize jsou evidované odděleně.

## Technická kontrola

Prostředí: Python 3.14.5, Zola 0.23.4, Pagefind 1.5.2. CI používá Python 3.12 a Node.js 22; vzdálený GitHub workflow zde nebyl spuštěn.

| Kontrola | Výsledek |
|---|---|
| Jednotkové testy | **22/22 prošlo**: matematika, odkazy, fragmenty, konfigurace hledání, sousední témata a ochrana výstupních složek |
| Obsah | **169 stránek**: AJ 20, ČJL 97, ASW 26, PSP 26; čísla, metadata, povinné části, odkazy a pokrytí rozcestníky v pořádku |
| Produkční sestavení | `py -3 scripts/build.py` prošlo pro `https://sdragonex.github.io/Maturita` |
| Zola | Kontrola vnitřních odkazů a sestavení bez chyby; externí odkazy se hromadně neověřují |
| Pagefind | **179 indexovaných stránek**, jazyk `cs`; zahrnuje také rozcestníky a průvodce |
| Výstupní HTML | Lokální soubory, fragmenty, čeština, konfigurace hledání a sousední témata v pořádku |
| Kořen webu | Sestavení a validátor prošly pro `http://127.0.0.1:8766` |
| Podcesta | Sestavení a validátor prošly pro `http://127.0.0.1:8765/Maturita` |
| PDF přes HTTP | Všechny tři soubory vracejí HTTP 200, `application/pdf` a úvodní signaturu PDF |
| Kontrola změn | `git diff --check` po úpravě zápisu zalomení v AJ bez chyb |

Pagefind očekávaně vynechává přesměrovací dokument `posts/page/1/` bez obalu HTML a upozorňuje, že pro češtinu nepodporuje stemming. Hledání bez diakritiky funguje; automatické spojování všech tvarů českých slov tím není zaručeno.

## Prohlížeč

Místní náhled byl zkoušen v prohlížeči Codex při šířkách 1280, 390 a 320 px. U kontrolovaného článku PSP, úvodu a seznamu 97 knih nebyl zjištěn vodorovný přesah dokumentu:

- Pod `/Maturita/` hledání `EtherChannel` a Enter otevřely PSP 10 se správnou adresou.
- V kořeni webu hledání `rimanka` našlo *Moravia, A.: Římanka* a Enter otevřel příslušnou stránku.
- Neexistující heslo zobrazilo české oznámení bez výsledků. Escape zavřel nabídku hledání.
- Mobilní panel převzal zaměření a znepřístupnil podklad; Escape jej zavřel s návratem zaměření na původní tlačítko.
- Na PSP 10 fungovalo odkrytí odpovědi a odkaz na PDF vedl do správné podcesty. Dostupnost PDF je doložena také kontrolou HTTP.
- Na počítači jsou přímo dostupné předměty v postranním panelu. Kontrolován přepínač motivu a zachování volby po obnovení.

Zkouška odhalila a oprava odstranila načítání `/pagefind/` místo `/Maturita/pagefind/`. `pagefind-config` nyní výslovně nastavuje `bundle-path` a `base-url` včetně závěrečného lomítka; validátor obě hodnoty kontroluje. Opraven byl také obrácený směr sousedních témat, úzké mobilní hledání a chybějící přístupný popisek vstupu.

Nejde o audit každé stránky na všech zařízeních ani o úplný audit přístupnosti. Tisk a vykreslení PDF v různých prohlížečích nejsou tímto potvrzeny.

## Obsahová revize

Všech 169 témat má studijní text. Automatický validátor potvrzuje strukturu a pokrytí, **nikoli správnost každého tvrzení**. Literární stránky jsou stručné přehledy pro další práci s četbou. Odborné příklady jsou úkoly k provedení, nikoli záznam o úspěšné laboratorní zkoušce.

Cíleně bylo redakčně přečteno **37 přehledů**:

- ČJL: 4, 14, 15, 16, 24, 29, 39, 47, 49, 50, 55, 61, 65, 69, 79, 83, 88, 90, 91, 96.
- PSP: 3, 6, 7, 8, 10, 14, 17, 18, 19, 20, 21, 22, 23.
- ASW: 17, 22, 24, 25.

Externí zdroje byly cíleně použity pro šest oprav nebo zpřesnění; odkazy jsou u příslušných textů:

| Stránka | Oprava nebo zpřesnění |
|---|---|
| ČJL 15 | Posloupnost Tomanovy cesty podle úplného textu a rozlišení balady od sbírky |
| ČJL 69 | *Šlépěje* patří do Povídek z jedné kapsy; odstraněna záměna se *Šlépějí* z Božích muk |
| PSP 7 | Síťový prefix nezávisí jen na shodě prvních oktetů; příklad dvou `/26` a poznámka k `/31` |
| PSP 10 | LACP vyžaduje alespoň jednu stranu `active`; odlišen statický režim `on` |
| PSP 21 a 22 | Správné `INotifyPropertyChanged`, rozlišení události a aktualizace vazby; opraveno vykreslení generických typů |

Tento vzorek nemá potvrzení každé věty z primárních zdrojů. Zbývá systematická revize podle konkrétních vydání, provedení IT úkolů v určeném prostředí a soustavná jazyková revize AJ.

## Platnost a zbývající vstupy

Průvodce uvádí kontrolu oficiálních zdrojů k **9. 9. 2026**. Jarní interval 3.–6. 5. 2027 dokládá sdělení MŠMT; neurčuje den a čas jednotlivých předmětů. Školní dokumenty uložené v projektu jsou z roku 2026. Přesné podzimní termíny, školní rozpis, kritéria a platnost seznamů pro 2027 zatím nejsou doloženy.

Chybí osobní seznam 20 knih a schválené zadání maturitní práce. U nejednoznačných výborů a cyklů musí škola potvrdit rozsah. Nová verze nebyla publikována; protokol dokládá místní sestavení.

## Opakování kontrol

```powershell
py -3 scripts/build.py
py -3 scripts/build.py --preview
py -3 scripts/build.py --base-url http://127.0.0.1:8766 --output-dir temp/root-site
```

Pracovní logy jsou pouze místně v ignorované složce `temp/`; v repozitáři je tento protokol. Po změně závislostí, šablon či obsahu zopakuj odpovídající kontrolu a zapiš nový výsledek.

[Dokumentace](README.md) · [Plán](PLAN.md) · [Obsah a zdroje](OBSAH.md) · [Údržba](UDRZBA.md)
