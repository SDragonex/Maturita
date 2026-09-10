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

Všech 169 témat má studijní text. Automatický validátor potvrzuje strukturu a pokrytí, **nikoli správnost každého tvrzení**. Literární stránky jsou stručné přehledy pro další práci s četbou. Samotné zadání odborného příkladu nedokládá úspěšnou laboratorní zkoušku; konkrétně spuštěné ukázky mají samostatný záznam níže.

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

## Úpravy vzhledu a podkladů — 10. 9. 2026

Tento záznam se týká odstranění odběrů, tmavšího motivu, filtrů seznamů a metodiky podle nově dodaného PDF. Dřívější obsahová revize výše se tím nerozšiřuje.

| Kontrola | Výsledek |
|---|---|
| `py -3 scripts/build.py` | Úspěšné produkční sestavení pro `https://sdragonex.github.io/Maturita` |
| `py -3 scripts/build.py --preview` | Úspěšný náhled pod `/Maturita/` |
| `py -3 scripts/build.py --base-url http://127.0.0.1:8766 --output-dir temp/root-site` | Úspěšné sestavení v kořeni webu |
| Kontroly v sestavení | 22 úspěšných testů, 169 studijních stránek, Zola check/build, Pagefind (179 indexovaných stránek) a validátor místních odkazů |
| `node --check static/js/study.js` a `git diff --check` | Bez chyb |
| Odstranění odběrů | V žádném ze tří výstupů nejsou `atom.xml`, `rss.xml`, `feed.json` ani HTML odkazy na ně; konfigurace má `generate_feeds = false` |
| HTML bez spuštění JavaScriptu | Všechny rozcestníky obsahují původní počty 20 / 97 / 26 / 26 položek, tabulky ani řádky nejsou skryté; skrytý je pouze neaktivní filtr |
| Nové PDF přes HTTP | HTTP 200, `application/pdf`, 91 691 bajtů, signatura PDF a shodný SHA-256 s dodaným souborem |
| Rozbory knih | `git diff --name-only -- content/cjl` je prázdný; texty všech 97 rozborů nebyly v této etapě upraveny |

V prohlížeči Codex v náhledu pod `/Maturita/` byly ověřeny tyto případy:

- Literatura: `capek` vrací tři knihy, `capek bila` jednu; název `1984` vrací Orwellovu knihu č. 53 a číslo `6` jen Lakomce č. 6. Kategorie 19. století vrací 26 položek; její kombinace s Čapkem zobrazí českou zprávu bez výsledků. Zrušení filtru obnoví všech 97 knih.
- Odkaz „Přejít k seznamu“ umístí filtr pod horní navigaci. Skok z obsahu na kategorii skrytou filtrem obnoví seznam a odhalí cíl odkazu.
- AJ: `housing` vrací jedno téma z 20. ASW: `blender` vrací tři témata z 26. PSP: kategorie C# vrací 13 témat; následné číslo `21` jedno téma, které lze otevřít.
- Článek PSP 21 zobrazuje `21 z 26` a označuje aktivní předmět v navigaci. Globální hledání `EtherChannel` a Enter otevřou PSP 10 na správné adrese.
- Tmavé pozadí má vypočtenou barvu `rgb(11, 12, 14)`; přepnutí na světlý motiv vrátí bílou a tmavý motiv se zachová po přechodu na jinou stránku. Kontrolována také stránka 404 bez odkazů odběrů.
- Při šířce 320 px se ovládání filtru skládá pod sebe, kategorie se vejde do stránky a kombinace slov vrací správný výsledek. Dokument nemá vodorovný přesah. Kontrolováno také zobrazení na počítači.

Zdrojové PDF bylo přečteno včetně členění částí a označení **© 2014 CZVV, verze 1.0**. Metodika přebírá jeho osnovu, nepřipisuje mu termíny, bodování ani potvrzenou platnost pro rok 2027. Úprava osnovy jednotlivých rozborů zůstává výslovně odložená.

Tiskové CSS nyní vynucuje světlý motiv a ponechává počet výsledků, aby filtrovaný tisk nepůsobil jako úplný seznam. Tiskový dialog, vícestránkový výstup a automatické rozbalení odpovědí nebyly ověřeny. Stejně tak nejde o úplný audit přístupnosti, všech mobilních zařízení ani o nové vzdálené nasazení.

## Řešené odborné příklady — pokračování 10. 9. 2026

Rozšířeny byly pouze PSP 7 a PSP 21. Číslování a informace o nepotvrzených školních podkladech 2027 zůstaly zachovány.

| Téma | Provedené ověření |
|---|---|
| PSP 7: IPv4 | Přesný blok Pythonu z Markdownu spuštěn v Pythonu 3.14.5; výstup automaticky porovnán s článkem. Ověřeny masky, síť, broadcast, rozsahy a 62 hostitelských adres pro oba `/26`. Další výpočty prověřily úkol `.190/.194`, změnu na `/24`, čtyři podsítě a výjimky `/31` a `/32`. |
| PSP 21: kolekce C# | Přesný blok C# z Markdownu přeložen kompilátorem Roslyn ze SDK 10.0.400 s nullable a varováními jako chybami; spuštěn na .NET 10.0.11. Osm řádků výstupu se přesně shoduje s článkem. |
| Varianty C# | Odebrání oznámení změny odstranilo pouze řádek `Vlastnost: Nazev`; změněný název ve slovníku zůstal. Po odebrání knihy z kolekce vrací samostatný slovník `ContainsKey(1) == true`. |
| Nezávislá kontrola textu | Oba rozšířené zdrojové články prošly další kontrolou výpočtů a vysvětlení bez konkrétního nálezu; nejde o plošnou revizi ostatních témat. |

Výchozí `dotnet run` a následný restore s místní konfigurací zastavilo odepřené čtení uživatelského `NuGet.Config`. Pro ověření programu byl proto použit přímo místní `Roslyn/bincore/csc.dll`, referenční sestavení `Microsoft.NETCore.App.Ref/10.0.11/ref/net10.0`, vlastní `runtimeconfig.json` a spuštění výsledné DLL přes `dotnet`. Externí balíčky nebyly potřeba. To dokládá překlad a chování ukázky, nikoli úspěšný průchod NuGet restore v tomto omezeném prostředí. Pracovní soubory a výstupy variant jsou v ignorované složce `temp/overeni-kolekce/`.

Zdroje jsou uvedené přímo u textů: RFC 4632 a RFC 3021, dokumentace Pythonu a Microsoft Learn pro `TryGetValue`, `TryAdd`, `ObservableCollection` a oznámení změny vlastnosti. Síťový výpočet nepotvrzuje konektivitu skutečných zařízení a konzolové události nenahrazují ověření datové vazby v okně WPF.

V prohlížeči byly ověřeny vykreslené generické typy C#, rozbalení očekávaného výstupu a kontrola úkolu IPv4. Záhlaví i metadata změny ukazují `updated = 2026-09-10`. Mobilní kontrola při 320 px odhalila přesah dlouhého nadpisu a širokých tabulek; opraveno zalamováním nadpisů a posunem uvnitř tabulek. Po opravě mají obě stránky šířku dokumentu 305 px při dostupné šířce 305 px, tabulku lze posunout šipkou doprava a kód má vlastní posuvnou oblast. Odstavce a tabulky v rozbalených řešeních mají sjednocené styly. Opět zkontrolován filtr literatury `capek`: tři knihy a bez vodorovného přesahu dokumentu.

Po závěrečných úpravách znovu prošla produkční sestava, náhled pod `/Maturita/` i sestava v kořeni: 22 testů, 169 témat, 179 indexovaných stránek a kontrola místních odkazů. Texty `content/cjl/` zůstávají beze změny. Nové příklady ani úpravy vzhledu nebyly vzdáleně nasazeny.

## Opakování kontrol

```powershell
py -3 scripts/build.py
py -3 scripts/build.py --preview
py -3 scripts/build.py --base-url http://127.0.0.1:8766 --output-dir temp/root-site
```

Pracovní logy jsou pouze místně v ignorované složce `temp/`; v repozitáři je tento protokol. Po změně závislostí, šablon či obsahu zopakuj odpovídající kontrolu a zapiš nový výsledek.

[Dokumentace](README.md) · [Plán](PLAN.md) · [Obsah a zdroje](OBSAH.md) · [Údržba](UDRZBA.md)
