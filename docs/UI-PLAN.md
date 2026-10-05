# Plán rozhraní, vzhledu a studijního formátování

**Datum:** 22. 9. 2026. **Stav:** návrh připravený k postupné realizaci. **Aktuální zadání:** soustředit se na rozhraní a čitelnost; rozsáhlé úpravy učiva nyní odložit.

## 1. Co má rozhraní studentovi umožnit

Najít konkrétní téma, pochopit jeho strukturu, pohodlně je číst, vyřešit úkol a vrátit se k dalšímu tématu. Tomu odpovídá hlavní cesta **předmět → seznam → téma → procvičení → další téma**.

Vizuální směr: klidná digitální učebnice s přehledným ovládáním. Zachovat stávající tmavý motiv a nabídnout stejně propracovaný světlý. Výklad má být nejvýraznější částí stránky. Barva, rámeček a ikona mají vyjadřovat konkrétní význam; běžné odstavce zůstanou v souvislé čtecí ploše.

**Samostatný [vizuální prototyp studijní stránky](prototypes/studijni-stranka.html)** ukazuje návrh rozložení a formátování. Je to podklad k rozhodování, není napojený do produkčních šablon. Jeho krátký ukázkový text není obsahovou revizí učiva.

## 2. Z čeho návrh vychází

Prohlédnuty aktuální šablony, Sass a `static/js/study.js`. Dne 22. 9. proběhlo místní sestavení náhledu: **22/22 testů, kontrola 169 studijních stránek, build Zoly a index Pagefind prošly**. Jde o výchozí technický stav, nikoli ověření budoucího návrhu nebo úplný audit přístupnosti.

V prohlížeči byly prohlédnuty úvod, dlouhé téma PSP 7 a katalog literatury; PSP 7 při šířce 1440 a 390 CSS px, katalog na mobilu. Zjištění:

| Pozorování | Dopad | Navržená změna |
|---|---|---|
| U PSP 7 na desktopu má navigace přibližně 356 px a odstavec 774 px při písmu 16 px | Velká boční plocha a dlouhé řádky | Kompaktní navigace a omezená délka čtecího řádku |
| Navigace je centrovaná uprostřed levého panelu, obsah článku začíná výrazně výš | Horší vizuální návaznost a využití místa | Navigace zarovnaná vlevo od horního okraje |
| Obsah tématu je nahoře v zavřeném bloku | Při čtení není po ruce struktura dlouhého textu | Trvale dostupný obsah na široké obrazovce, dostupný přepínač na mobilu |
| Na 390 × 844 začíná první kapitola PSP 7 přibližně v 520 px | Název, přehled a opakovaný návrat odsouvají učivo | Kratší hlavička článku a jediný zřetelný návrat |
| Mobilní katalog literatury nejdřív opakuje titul, popis, ročník a pravidla | Filtr a vlastní knihy nejsou v první obrazovce | Samostatná šablona katalogu s filtrem u názvu a pravidly v samostatném bloku |
| Nadpisy přidávají `#`, `##`, `###`, linky i různé styly | Více dekorací než funkčních rozdílů | Hierarchie velikostí, váhy a rozestupů; kotva jen při zaměření |
| Typografie kombinuje STIX, Ysabeau, Dancing Script a zbytky odkazů na nenačítané fonty | Ovládání a výklad působí nesourodě | Jedna rodina pro rozhraní, jedna pro čtení, monospace pro kód |
| Styly vnořeného textu a rozbalených řešení jsou oddělené od běžných odstavců | Stejný text může mít rozdílné odsazení | Společná typografie pro text v libovolném podporovaném bloku |

Další rizika z kódu, která je potřeba při realizaci reprodukovat: nadpisy nemají společný posun vůči pevné hlavičce; tiskový reset neodstraňuje procentní šířku a plovoucí zarovnání obsahu; tabulky a kód mají více způsobů horizontálního posouvání. Tato zjištění nejsou tvrzením o dokončeném tiskovém testu.

## 3. Základ vzhledu a typografie

Hodnoty níže jsou výchozí návrh k ověření na skutečných stránkách, ne již naměřené parametry hotové změny.

| Prvek | Návrh |
|---|---|
| Běžný výklad | 18 px / řádkování 1,65–1,75; jednotky `rem`; STIX Two Text s Georgia/serif fallbackem |
| Navigace, tlačítka, filtry, metadata | `system-ui`, 15–16 px; drobná pomocná metadata nejméně 14 px |
| Čtecí řádek | Přibližně 65–70 znakových jednotek `ch`, výchozí maximum 68ch |
| Nadpis tématu | 34–40 px desktop, 28–32 px mobil; bez vynuceného počtu řádků |
| H2 / H3 / H4 | Přibližně 28 / 22 / 19 px; jednotné mezery a logické úrovně |
| Kód | `ui-monospace`, Consolas, monospace; 15–16 px, řádkování 1,55; bez zmenšování dlouhého kódu do nečitelna |
| Odstavce a seznamy | Shodná levá hrana a čtecí šířka; mezi odstavci přibližně 1em |
| Rozestupy | Společná škála 4 / 8 / 12 / 16 / 24 / 32 / 48 px |
| Světlý motiv | Jemně teplé pozadí `#f8f7f4`, tmavý text, bílé nebo mírně odlišené doplňkové plochy |
| Tmavý motiv | Zachovat základ `#0b0c0e`; rozlišit pozadí, doplňkové plochy a ohraničení |
| Akcent | Tlumená tyrkysová pro aktivní prvek a odkaz; konkrétní odstíny ověřit kontrastem v obou motivech |
| Vizuální rytmus | Zarovnání vlevo, omezené rámečky, měkké rohy 6–8 px, minimum stínů |

Tučné a kurzivní písmo dědí rodinu svého bloku. Anglické názvy, česká diakritika, číslice, interpunkce a monospace se ověří dohromady. Odkazy v textu zůstanou podtržené a rozpoznatelné i bez barvy. Animované psaní motta se nahradí statickým popisem; po otevření tématu se text nemá pohybovat.

## 4. Rozložení obrazovek

### Široká obrazovka od přibližně 1280 px

Kompaktní hlavička výšky přibližně 56–64 px. Pod ní grid se třemi oblastmi: **předměty 220 px / čtení do 68ch / obsah tématu přibližně 200 px**. Mezery 24–32 px. Nadpisy a čtení mají stejnou osu. Boční části zůstávají dostupné při posunu stránky; vlastní čtení používá hlavní posuvník prohlížeče.

Levý panel ukazuje předměty, maturitní práci, pravidla a studijní plán. Aktuální předmět má textové i vizuální označení. Pravý panel obsahuje názvy kapitol a zvýrazňuje aktuální kapitolu; označení při posouvání samo nepřesouvá fokus ani nepřepisuje historii.

### Střední obrazovka přibližně 961–1279 px

Dva sloupce: kompaktní navigace a čtení. Obsah tématu se přesune do jednoho rozbalovacího ovladače nad výklad. Rozhraní nesmí zmenšovat text, aby udrželo tři sloupce za každou cenu.

### Mobil a tablet do přibližně 960 px

Jednosloupcové čtení s okraji 16–20 px. Hlavička obsahuje pojmenované menu, vyhledávání a nastavení čtení. Otevřené menu zachová existující Escape, izolaci fokusu pomocí `inert` a jeho návrat do otevíracího tlačítka.

Ovládání „Obsah tématu“ bude dostupné i po odrolování úvodu, bez překrytí odstavců. Použít kompaktní řádek v hlavičce nebo pod ní a zahrnout jeho výšku do posunu kotev. Tři plovoucí lišty současně nejsou potřeba. Dlouhé názvy se zalamují přirozeně.

## 5. Jednotlivé stránky

### Domů

- Kratší úvod s jasným názvem projektu, hledáním a přímým vstupem do čtyř předmětů.
- Předměty zobrazit jako čtyři přehledné položky s názvem, skutečným počtem témat a jednovětým popisem.
- Pravidla, studijní plán a maturitní práce mají samostatné dobře viditelné vstupy.
- Stav platnosti podkladů uvést jednou v kompaktním upozornění s odkazem na vysvětlení; zachovat jeho význam i dostupnost.
- Osobní projekty a informace o autorovi přesunout do sekundární navigace/patičky.

### Seznam předmětu

- Název, stručný kontext, filtr a počet výsledků umístit před dlouhou metodiku.
- Pravidla a PDF ponechat v jasně pojmenovaném bloku „Pravidla a podklady“. Důležité upozornění na platnost ponechat viditelné i při jeho zavření.
- Při 97 knihách používat kompaktní řádky; číslo, autor a název mají rozlišitelnou hierarchii. Nevytvářet 97 rozměrných karet.
- Zachovat hledání bez diakritiky a filtrování kategorií. Rozlišit „Hledat v celém webu“ a „Filtrovat tento seznam“.
- Zachovat dotaz, kategorii a pozici při návratu z tématu; přednostně přes URL parametry a běžnou historii, bez povinného účtu.
- Prázdný výsledek nabídne „Zrušit filtr“. Počet položek oznámit pomocí současného živého stavového textu.
- Řádky se na mobilu zalomí do kompaktního seznamu; dlouhý název nesmí vytlačit číslo mimo obrazovku.

### Studijní téma

V horní části: drobečková navigace, název, číslo tématu a stručná anotace, pokud přináší novou informaci. Datum aktualizace je vedlejší údaj. Zrušit opakování stejného návratu a názvu v úvodu při zachování všech cílových URL a potřebných kotev.

Po úvodu následuje výklad se stabilními nadpisy a dostupným obsahem. Na konci zůstanou zdroje a předchozí/další téma. Výklad má zůstat souvisle čitelný; rozbalování se použije hlavně pro řešení a doplňující podrobnosti.

### Vyhledávání

Použít stávající Pagefind. Výsledek má ukázat název, předmět a krátký úryvek. Případné filtrování podle předmětu zavést až s odpovídajícím indexem, ne jen jako prázdný ovladač. Na mobilu výsledky využijí dostupnou šířku. Zajistit stavy načítání, nenalezeno a selhání indexu s cestou zpět na seznam předmětů.

## 6. Formátovací systém pro budoucí obsah

Připravit malé množství opakovatelných prvků. Uvnitř všech bloků musí fungovat odstavce, víceúrovňové seznamy, odkazy, tabulky, kód a nadpisy stejně jako v běžném výkladu.

| Typ obsahu | Vzhled a chování |
|---|---|
| Výklad / definice | Souvislý text, zvýrazněný pojem, bez zbytečného rámečku kolem každého odstavce |
| Důležitá informace | Úzký akcent, český název a stručný text; odlišný od literární citace |
| Častá chyba | Štítek „Častá chyba“, decentní varovný odstín a vysvětlení; význam není pouze v barvě |
| Řešený příklad | Zřetelně oddělené zadání, postup a výsledek; očíslované kroky zachovají čtecí rytmus |
| Otázka a řešení | Viditelná otázka, ovladač „Zobrazit řešení“, sémantické `details/summary`; neskrývat základní výklad |
| Kód | Název jazyka, tlačítko kopírování se stavem úspěchu/chyby, jeden posuvný obal; výstup odlišit popiskem |
| Tabulka | Čitelná hlavička, horní zarovnání víceřádkových buněk; číselné údaje vhodně zarovnané; přesah řešit lokálně |
| Slovníček EN/CZ | Jasné párování dvou jazyků, prostor pro delší překlad, označení angličtiny `lang="en"` |
| Modelový projev AJ | Souvislý anglický text v samostatné čtecí ploše; upozornění na modelový příklad u jeho začátku |
| Literární ukázka | Zachovat odstavce a verše, místo pro vydání a stránku; citaci nezaměňovat za informační upozornění |
| Literární rozbor | Připravit vzhled metadat, částí osnovy a práce s výňatkem, aniž se nyní přepisuje všech 97 textů |
| Obrázek / schéma | Alternativní text, čitelný popisek, přirozený poměr stran; světlé diagramy neinvertovat automaticky |
| Vzorec / výpočet | Čitelný zápis, vysvětlení proměnných, bezpečný přesah na mobilu; zachovat současné zpracování matematiky |
| Zdroj / platnost | Malý, ale čitelný závěrečný blok; odlišit datum úpravy od data ověření zdroje |

Vytvořit také **neindexovanou vzorovou stránku formátování** se všemi prvky, dlouhými českými názvy, diakritikou a jejich vnořením. Bude sloužit pro kontrolu budoucích změn. Nejde o nové učivo ani o novou veřejnou sekci webu.

## 7. Nastavení čtení a tisk

Po stabilizaci základního rozložení doplnit malý panel „Vzhled a čtení“: světlý/tmavý/systémový motiv, velikost textu 18/20/22 px a návrat k výchozím hodnotám. Při nepřístupném místním úložišti má čtení i přepínání fungovat pro aktuální návštěvu.

Tisk musí mít vlastní světlý layout přes dostupnou šířku, bez navigace, plovoucích panelů a tlačítek. Nadpis se nesmí ocitnout sám na konci stránky; hlavička tabulky se má opakovat. Dlouhý blok se musí dát rozdělit, ne oříznout zákazem zalomení.

Téma nabídne „Tisk bez řešení“ a „Tisk včetně řešení“. U katalogu rozlišit aktuální filtrovaný výběr a celý seznam. Před tiskem dočasně upravit pouze potřebný stav; po tisku i jeho zrušení obnovit otevření odpovědí, filtr a fokus. Ověřit také přímý tisk přes Ctrl+P a uvést jeho výchozí chování.

Ukládání naučených témat, osobní poznámky nebo kartičky tvoří případnou další funkční etapu. Nejsou podmínkou tohoto redesignu; samotné otevření článku se nesmí vydávat za zvládnutí látky.

## 8. Postup realizace po ověřitelných etapách

| Pořadí | Balík úprav | Dotčené části | Dokončeno, když |
|---|---|---|---|
| **1 — základ čtení** | Typografické proměnné, jednotné odsazení a šířky, čisté nadpisy, dědění uvnitř bloků | `sass/_variables.scss`, `_base.scss`, `_content.scss`, `_components.scss`, `_study.scss` | Housing, Lakomec a PSP 7 jsou souvisle čitelné na mobilu i desktopu; žádný horizontální posuv celé stránky |
| **2 — orientace** | Kompaktní navigace, kratší úvod, dostupný obsah, aktivní kapitola a správné skoky | `templates/_base.html`, `page.html`, nové drobné partialy, `_sidebar.scss`, `_topbar.scss`, `static/js/study.js` | Ke kapitole a seznamu lze dojít klávesnicí i dotykem; skok nezakryje nadpis |
| **3 — katalog a hledání** | Samostatná šablona katalogu, filtry nahoře, kompaktní řádky, návrat k výsledkům | `templates/`, katalogové styly, `static/js/study.js`, Pagefind metadata | Fungují všechny čtyři předměty, nulový výsledek, návrat i přímý odkaz s filtrem |
| **4 — formátování učiva** | Jednotné příklady, řešení, upozornění, tabulky, kód, slovníček a citace | `templates/shortcodes/`, sdílené styly a vzorová stránka | Stejný typ bloku se všude chová stejně, včetně vnoření a dlouhého obsahu |
| **5 — čtení a tisk** | Nastavení písma a motivu, tisk tématu/seznamu, obnova dočasného stavu | Sdílené ovládání, JS pro čtení/tisk, samostatné tiskové styly | Tisk A4 je čitelný; zrušení dialogu nezmění studijní stav |
| **6 — sjednocení a kontrola** | Zkrácení domovské stránky, sekundární odkazy, doladění detailů a kontrola všech typů stránek | `templates/index.html`, `_home.scss`, `docs/OVERENI.md` | Regresní matice níže projde a protokol obsahuje skutečné výsledky |

**První prováděcí krok:** převést typografii a rozložení na třech referenčních tématech a katalogu literatury. Po vizuální kontrole rozšířit stejná pravidla na zbytek webu. Každá etapa končí kontrolou na stejných stránkách; nové prvky nevytvářet jako další vrstvu soupeřících CSS přepisů.

## 9. Pravidla implementace

- Zachovat Zolu, Markdown a Pagefind; návrh nevyžaduje přechod na jiný framework nebo backend.
- Rozlišit obal aplikace, katalog, hlavičku tématu, čtecí typografii a studijní komponenty. Sdílená pravidla definovat na jednom místě.
- Pro nové zarovnání použít grid/flex a jednu sadu responzivních okrajů; odstranit konfliktní `float`, procentní sloupce a `90vw` na jednotlivých odstavcích až po jejich nahrazení.
- Běžný Markdown musí vypadat dobře i bez shortcode. Shortcode používat pro sémantiku příkladu/řešení, ne pro každý nadpis či odstavec.
- Neodvozovat druh bloku nebo předmět z volného textu nadpisu; využít existující metadata a jednoznačné značky.
- Zachovat URL témat, jejich pořadí a existující kotvy. Podcesta `/Maturita/` musí fungovat i v nových ovládacích prvcích.
- Obsah a navigace musí zůstat dostupné bez JavaScriptu. Stav vyhledávání a doplňkových funkcí má být srozumitelný při jejich selhání.
- Převody markup a metadat potřebné k novému formátování oddělit od věcných úprav studijních textů.
- Nevytvářet nové automatické kontroly čistě podle počtu CSS tříd. Testovat výsledné chování, odkazy, zachování stavu a kritické scénáře.

## 10. Jak poznáme, že výsledek funguje

### Vizuální a funkční matice

Kontrolovat **320, 390, 768, 1024, 1440 a 1920 px**, oba motivy a zvětšení textu. Výchozí srovnávací stránky:

- Úvod a literatura se všemi 97 položkami, včetně nulového výsledku.
- AJ 1 Housing: EN/CZ tabulka, souvislá angličtina a otázky.
- Lakomec: metadata a hierarchie rozboru.
- PSP 7: dlouhý text, výpočet, tabulka, kód a více skrytých řešení.
- PSP 21: C# kód a očekávaný výstup.
- Budoucí vzorová stránka: obrázek, matematika, citace, dlouhý odkaz a vnořené komponenty.

### Akceptační kritéria

- [ ] Téma, předmět a aktuální kapitola jsou rozpoznatelné bez hledání v několika navigacích.
- [ ] U běžného referenčního tématu je na 390 × 844 vidět začátek učiva bez prvního posunu; dlouhý název se nesmí kvůli tomu ořezat.
- [ ] U seznamu je filtr dostupný v první mobilní obrazovce; hlavní upozornění na platnost je stále dostupné a srozumitelné.
- [ ] Hlavní text má navrženou velikost a omezenou délku řádku; stránka nevyžaduje vodorovný posuv. Výjimky typu široké tabulky jsou řešené uvnitř vlastního obalu.
- [ ] Běžný text dosahuje kontrastu alespoň 4,5 : 1; velký text alespoň 3 : 1. Kontrast se měří také u metadat, placeholderů a zvýraznění kódu.
- [ ] Fokus je vždy viditelný, ovladače mají popis a hlavní dotykové ovládání cílí na plochu alespoň 44 × 44 CSS px. Jde o návrhový cíl; minimum WCAG 2.2 AA je 24 × 24 px s definovanými výjimkami.
- [ ] Rozhraní zůstává funkční při 200% zvětšení textu a při reflow odpovídajícím 320 CSS px, včetně 400% zoomu desktopu. Změna uživatelských rozestupů text neořízne.
- [ ] Všechny nové panely lze otevřít/zavřít klávesnicí; návrat fokusu, Escape a pořadí ovládání jsou ověřené.
- [ ] Přímý odkaz na kapitolu skončí pod pevnou hlavičkou. Obsah i vyhledávání mají správnou pozici ve světlém/tmavém motivu.
- [ ] Tisk včetně/skrytí řešení i jeho zrušení mají předvídatelný výsledek a obnoví předchozí stav.
- [ ] Bez JS lze přečíst text a přejít mezi předměty; selhání fontu, úložiště nebo vyhledávání nezablokuje čtení.
- [ ] Po každé etapě projdou stávající testy, kontrola obsahu, Zola a Pagefind. Závěrem ověřit kořen i podcestu podle projektové údržby.

Podklady pro měřitelná kritéria: W3C [kontrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [velikost ovládacích cílů](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [uživatelské rozestupy textu](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html). Stanovení těchto kritérií samo nedokládá shodu celé aplikace s WCAG.

## 11. Rozsah tohoto kroku

Tento krok připravuje plán a samostatný vizuální prototyp. Produkční vzhled ani učební texty se tímto plánem nemění. Odložené přepracování literárních rozborů zůstává samostatným úkolem. Stávající ročník, podklady a publikační režim nejsou předmětem změny.

[Dokumentace](README.md) · [Celkový plán](PLAN.md) · [Protokol ověření](OVERENI.md)
