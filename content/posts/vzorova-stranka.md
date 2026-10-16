+++
title = "Vzorová stránka formátování učiva a komponent"
description = "Interní referenční přehled všech komponent, typografie, studijních bloků a formátovacích prvků pro ověření vzhledu a budoucí kontroly změn."
date = 2026-10-16
template = "page.html"
[extra]
author = "Dany Chaker"
unindexed = true
+++

Tato stránka slouží jako **interní vizuální a technický testbed** pro ověření všech komponent studijního rozhraní, typografie, responzivity, tisku a přístupnosti podle [plánu uživatelského rozhraní](@/posts/studijni-plan.md). Stránka není součástí veřejného indexu a vyhledávání Pagefind ji vynechává.

## 1. Základní čtecí typografie a hierarchie

Text učiva používá promyšlené měřítko písma, pohodlnou výšku řádku a maximální šířku řádku `68ch`. Všechny odstavce zachovávají přirozený čtecí rytmus bez umělých rámečků.

V souvislém textu lze používat **důležité pojmy**, *zvýrazněné výrazy*, inline kód jako `IPAddress.Parse("192.168.1.1")`, klávesové zkratky a [odkazy na rozcestník přípravy](@/posts/rozcestnik.md).

### Podnadpis třetí úrovně pro dílčí logické celky

Pro přehlednost témat se používají podnadpisy H3 a H4, které mají zřetelné odsazení shora a těsnější vazbu k následujícímu odstavci:

- Odrážkový seznam první úrovně s vysvětlením klíčového konceptu.
- Druhá odrážka s vnořeným seznamem:
  - Podrobnější technický detail nebo výjimka z pravidla.
  - Odkaz na oficiální dokumentaci nebo normu.
- Třetí odrážka s doporučeným postupem pro ústní zkoušku.

#### Podnadpis čtvrté úrovně pro dílčí parametry

Číslovaný seznam kroků zachovává přehlednou posloupnost:

1. Prověř výchozí stav síťového rozhraní nebo zadání úlohy.
2. Zvol vhodný algoritmus nebo konfiguraci.
3. Ověř funkčnost výsledného řešení pomocí diagnostického nástroje.

## 2. Informační boxy a upozornění (Callouts)

Informační boxy se používají střídmě a mají zřetelnou sémantiku i barevný akcent pro světlý i tmavý AMOLED režim.

<aside class="study-callout study-callout-note" role="note">
  <div class="callout-header">
    <span class="callout-icon" aria-hidden="true"><i class="fa-solid fa-circle-info"></i></span>
    <span class="callout-title">Poznámka k metodice</span>
  </div>
  <div class="callout-body">
    <p>Základní informační poznámka doplňuje kontext výkladu, aniž by přerušovala souvislé čtení.</p>
  </div>
</aside>

<aside class="study-callout study-callout-tip" role="note">
  <div class="callout-header">
    <span class="callout-icon" aria-hidden="true"><i class="fa-solid fa-lightbulb"></i></span>
    <span class="callout-title">Tip pro ústní zkoušku</span>
  </div>
  <div class="callout-body">
    <p>U ústní odpovědi začni vždy obecnou definicí a praktickým příkladem ze života, teprve poté přejdi k podrobnostem implementace.</p>
  </div>
</aside>

<aside class="study-callout study-callout-important" role="note">
  <div class="callout-header">
    <span class="callout-icon" aria-hidden="true"><i class="fa-solid fa-circle-exclamation"></i></span>
    <span class="callout-title">Důležité pravidlo</span>
  </div>
  <div class="callout-body">
    <p>U každé podsítě IPv4 musí zůstat první adresa vyhrazena pro identifikaci sítě a poslední adresa pro všesměrové vysílání (broadcast).</p>
  </div>
</aside>

<aside class="study-callout study-callout-warning" role="note">
  <div class="callout-header">
    <span class="callout-icon" aria-hidden="true"><i class="fa-solid fa-triangle-exclamation"></i></span>
    <span class="callout-title">Varování před nekompatibilitou</span>
  </div>
  <div class="callout-body">
    <p>Při konfiguraci agregačního protokolu LACP musí být alespoň jedna strana nastavena v aktivním režimu <code>active</code>, jinak se kanál nesestaví.</p>
  </div>
</aside>

<aside class="study-callout study-callout-mistake" role="note">
  <div class="callout-header">
    <span class="callout-icon" aria-hidden="true"><i class="fa-solid fa-circle-xmark"></i></span>
    <span class="callout-title">Častá chyba studentů</span>
  </div>
  <div class="callout-body">
    <p>Záměna události <code>PropertyChanged</code> za samotnou aktualizaci vazby ve WPF. Bez vyvolání události se změna hodnoty v paměti neprojeví v uživatelském rozhraní.</p>
  </div>
</aside>

Rovněž standardní GitHub alerty zapsané v Markdownu přebírají jednotné styly:

> [!NOTE]
> GitHub-style alert zapsaný v čistém Markdownu přebírá stejné barvy a typografii.

## 3. Řešené příklady a procvičování

Praktické odborné příklady mají zřetelně oddělené zadání, postup a výsledek.

<section class="study-example" aria-label="Výpočet použitelných adres podsítě /26">
  <div class="example-header">
    <span class="example-badge"><i class="fa-solid fa-calculator" aria-hidden="true"></i> ŘEŠENÝ PŘÍKLAD</span>
    <h4 class="example-title">Výpočet použitelných adres podsítě /26</h4>
  </div>
  <div class="example-body">
    <p><strong>Zadání:</strong> Zjistěte počet použitelných adres pro koncová zařízení v síti s prefixem <code>/26</code>.</p>
    <p><strong>Postup výpočtu:</strong></p>
    <ol>
      <li>Celková délka adresy IPv4 je <strong>32 bitů</strong>.</li>
      <li>Na klientskou část zbývá: <code>32 - 26 = 6 bitů</code>.</li>
      <li>Počet všech adres v podsíti je: 2<sup>6</sup> = 64 adres.</li>
      <li>Odečteme adresu sítě (všechny klientské bity 0) a broadcast (všechny bity 1): <code>64 - 2 = 62</code>.</li>
    </ol>
    <p><strong>Výsledek:</strong> Běžná podsíť <code>/26</code> nabízí <strong>62 použitelných adres</strong> pro síťová rozhraní.</p>
  </div>
</section>

## 4. Otázky a rozbalovací řešení

Otázky s interaktivním rozbalením řešení umožňují studentovi nejprve samostatně přemýšlet a až poté zkontrolovat správnou odpověď.

<div class="study-solution-block">
  <p class="solution-question"><strong>Otázka:</strong> Jaký je rozdíl mezi protokoly TCP a UDP z hlediska spolehlivosti?</p>
  <details class="solution-toggle">
    <summary class="solution-summary">
      <span class="solution-label">Zobrazit řešení a vysvětlení</span>
    </summary>
    <div class="solution-content">
      <ul>
        <li><strong>TCP</strong> je spojově orientovaný protokol s potvrzováním doručení, řízením toku a opětovným vysíláním ztracených paketů.</li>
        <li><strong>UDP</strong> je nespojovaný protokol bez záruky doručení a pořadí paketů, ale s minimální režií a nízkou latencí (vhodný pro DNS, VoIP, streamování).</li>
      </ul>
    </div>
  </details>
</div>

Pro zpětnou kompatibilitu funguje také nativní rozbalovací blok v Markdownu:

<details>
<summary>Kontrola odpovědi: Výchozí brána</summary>

Výchozí brána (Default Gateway) představuje IP adresu směrovače ve stejné podsíti, na kterou stanice posílá pakety určené pro cizí sítě.
</details>

## 5. Ukázky zdrojového kódu a konfigurace

Bloky kódu mají hlavičku s označením jazyka, plnou podporu horizontálního posuvu a přístupné tlačítko pro kopírování do schránky s dotykovým cílem 44 × 44 px.

```csharp
using System;
using System.Collections.ObjectModel;
using System.ComponentModel;

public sealed class Kniha : INotifyPropertyChanged
{
    private string _nazev = string.Empty;

    public string Nazev
    {
        get => _nazev;
        set
        {
            if (_nazev != value)
            {
                _nazev = value;
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof(Nazev)));
            }
        }
    }

    public event PropertyChangedEventHandler? PropertyChanged;
}
```

## 6. Strukturované tabulky s vodorovným posuvem

Tabulky se automaticky obalují responzivním kontejnerem s možností plynulého vodorovného posunu na malých obrazovkách bez přetečení celého dokumentu.

| Prefix | Maska podsítě | Počet adres | Použitelné adresy | Typické využití |
|:---|:---|---:|---:|:---|
| `/24` | `255.255.255.0` | 256 | 254 | Běžná LAN síť učebny nebo kanceláře |
| `/26` | `255.255.255.192` | 64 | 62 | Menší oddělení nebo zóna serverů |
| `/28` | `255.255.255.240` | 16 | 14 | Malá skupina tiskáren a infrastruktury |
| `/30` | `255.255.255.252` | 4 | 2 | Propojovací point-to-point linka směrovačů |

## 7. Anglický slovníček (EN / CZ) a modelový ústní projev

Pro anglický jazyk jsou připraveny dvojjazyčné dvojice a samostatné čtecí boxy pro souvislý modelový projev na úrovni B1/B2.

<div class="study-vocab-wrap">
  <dl class="study-vocab-pair">
    <dt><span class="vocab-en" lang="en">semi-detached house</span> <span class="vocab-phonetic">/ˌsem.i.dɪˈtætʃt haʊs/</span></dt>
    <dd><span class="vocab-cz">dvojdomek</span> <small class="vocab-note">(britská angličtina)</small></dd>
  </dl>
  <dl class="study-vocab-pair">
    <dt><span class="vocab-en" lang="en">mortgage</span> <span class="vocab-phonetic">/ˈmɔː.ɡɪdʒ/</span></dt>
    <dd><span class="vocab-cz">hypotéka, hypoteční úvěr</span> <small class="vocab-note">(finance a bydlení)</small></dd>
  </dl>
  <dl class="study-vocab-pair">
    <dt><span class="vocab-en" lang="en">household appliances</span> <span class="vocab-phonetic">/ˈhaʊs.həʊld əˈplaɪ.ən.sɪz/</span></dt>
    <dd><span class="vocab-cz">domácí spotřebiče</span> <small class="vocab-note">(lednička, pračka apod.)</small></dd>
  </dl>
</div>

<section class="study-speech" lang="en">
  <div class="speech-header" lang="cs">
    <span class="speech-badge"><i class="fa-solid fa-microphone-lines" aria-hidden="true"></i> MODELOVÝ ÚSTNÍ PROJEV (B1/B2)</span>
    <span class="speech-title">Housing and Living in a City</span>
  </div>
  <div class="speech-body">
    <p>I would like to speak about different types of housing and the advantages and disadvantages of living in a big city compared to a quiet village.</p>
    <p>In my opinion, living in a flat in a city center offers excellent accessibility to public transport, schools, sports centers, and cultural events. On the other hand, the cost of living and rent is generally higher, and there is often more noise and traffic congestion. Many young people prefer living in an apartment near their workplace, whereas families with children often search for a detached house with a private garden in suburban areas.</p>
  </div>
</section>

## 8. Literární ukázky a citace z děl

Literární výňatky z děl pro český jazyk a literaturu mají vyhrazený styl s citací autora, názvu a kontextu scény:

<blockquote class="literary-quote">
  <div class="literary-quote-body">
    <p>HARPAGON: Jak to se mnou mluvíš, ty drzoune? Koukej klidit se z mých očí, nebo tě přetáhnu holí!</p>
    <p>ŠIPEK: A proč mě vyháníte? Co jsem vám udělal?</p>
    <p>HARPAGON: Ty se ještě ptáš, co jsi udělal? Táhni, nebo tě probodnu! Už se na tebe nemohu ani podívat!</p>
  </div>
  <footer class="literary-quote-footer">
    <cite>
      <span class="quote-author">Molière:</span>
      <span class="quote-work">Lakomec</span>
      <span class="quote-source">1. dějství, výstup 3</span>
      <span class="quote-year">(1668)</span>
    </cite>
  </footer>
</blockquote>

## 9. Matematické výpočty a vzorce

Matematické výrazy jsou vykreslovány s vysokou čitelností a podporou zalomení na mobilních zařízeních:

Příklad vzorce pro výpočet Shannonovy kapacity přenosového kanálu:

$$C = B \cdot \log_2\left(1 + \frac{S}{N}\right)$$

Kde $C$ je maximální přenosová rychlost v bitech za sekundu, $B$ je šířka pásma v hertzích a $\frac{S}{N}$ je odstup signálu od šumu.

## 10. Obrázky, schémata a diagramy

Obrázky v textu využívají sémantický prvek `figure` s čitelným popiskem `figcaption`:

<figure class="study-figure">
  <img src="/Maturita/images/SSTE-WHITE.png" alt="SŠTE Brno logo" loading="lazy" decoding="async" width="180" />
  <figcaption class="study-figcaption">Ukázka grafického prvku školy se středovým zarovnáním a popiskem</figcaption>
</figure>

---

<section class="study-sources" aria-labelledby="zdroje-vzor">
  <h4 class="sources-heading" id="zdroje-vzor">Zdroje a ověření podkladů</h4>
  <p>Vzorová stránka byla vytvořena jako referenční podklad pro kontrolu konzistence a vizuální integrity studijního systému.</p>
  <div class="sources-meta">
    <span>Ověřeno: 16. 10. 2026</span>
    <span>Platnost podkladů: jaro a podzim 2027</span>
    <span>Autor design systému: Dany Chaker</span>
  </div>
</section>
