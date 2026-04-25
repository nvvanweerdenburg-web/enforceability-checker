# Dutch law enforceability ground taxonomy for RAG ingestion

This taxonomy maps every major ground of invalidity, nullity, or unenforceability under Dutch civil, procedural, and insolvency law into self-contained chunks suitable for a RAG pipeline serving a Netherlands-based legal enforceability checker. Each chunk is keyed by a stable `RAG_TAG`, preserves Dutch statutory terminology, and flags **confidence** levels per citation. All ECLI numbers listed as "verified" were confirmed on rechtspraak.nl or in published annotations during research; items marked "LOW CONFIDENCE" or "no clear leading HR case" should be treated as such by the retrieval layer.

A verification note up front: leading cases on foundational doctrines (Baris/Riezenkamp, Van Elmbt/Feierabend, Kribbebijter, Esmilo/Mediq, Heesakkers/Voets, Pouw/Visser, Briljant Schreuders/ABP, the Van Dooren q.q./ABN AMRO trilogy) were directly verified. Several older HR cases (pre-2000) carry ECLI numbers that were retrofitted by rechtspraak.nl and are correct but less canonical in older literature; these are still marked verified. Cases I could not conclusively verify within the research window are marked explicitly.

---

## PART A — MATERIAL VALIDITY GROUNDS (wilsgebreken, bekwaamheid, vorm, inhoud)

---

### A1. Handelingsonbekwaamheid — minderjarigheid & curatele
**RAG_TAG:** `nl.bw.3_32.handelingsonbekwaamheid`

- **Ground (NL/EN):** Handelingsonbekwaamheid / Legal incapacity (minors, persons placed under curatele).
- **Statutory anchor:** Art. 3:32 BW (capacity as rule); art. 1:234 BW (minderjarigen — limited capacity for normal age-appropriate transactions); art. 1:381 lid 2-3 BW (ondercuratelestelling); art. 1:32a BW (handlichting).
- **Legal qualification:** **Vernietigbaar** (art. 3:32 lid 2 BW). Not nietig of rechtswege.
- **Who can invoke:** Only the protected party — minor (through statutory representative) or person under curatele (through curator ex art. 1:381 lid 2 BW). **Not** invocable by the counterparty or the court ambtshalve.
- **Time limit:** Art. 3:52 lid 1 sub b BW — three years from the moment the incapacity ceased or the statutory representative became aware (for minors: from majority).
- **Partial nullity:** Yes, art. 3:41 BW in principle applicable, but because the whole rechtshandeling is affected by the incapacity, partial survival is usually not meaningful.
- **Leading HR cases:** No single dominant modern HR arrest; the regime is largely codified. Compare HR 5 januari 2001, ECLI:NL:HR:2001:AA9314 (capacity-adjacent, psychiatric patient) — **LOW CONFIDENCE** on direct relevance, treat as supplementary only.
- **Remedies:** Vernietiging ex tunc + restitution via art. 6:203 BW (onverschuldigde betaling); counterparty's protection via art. 1:234 lid 3 BW (gebruikelijke rechtshandelingen) and art. 3:35 BW only in very narrow circumstances.
- **Cross-refs:** A2 (geestelijke stoornis); C1 (bekrachtiging art. 3:58 BW).

---

### A2. Geestelijke stoornis zonder curatele
**RAG_TAG:** `nl.bw.3_34.geestelijke_stoornis`

- **Ground (NL/EN):** Geestelijke stoornis / Mental disorder without formal curatele.
- **Statutory anchor:** Art. 3:34 BW.
- **Legal qualification:** **Vernietigbaar**. Art. 3:34 lid 2 BW creates a **rebuttable presumption** that the rechtshandeling is nadelig if it was not evidently in the disturbed party's interest; in that case the wil is presumed te ontbreken and the act is vernietigbaar.
- **Who can invoke:** The party suffering the disorder (or its representative/heirs).
- **Time limit:** Art. 3:52 lid 1 sub b BW — three years after the disorder has ceased (or the representative learned).
- **Partial nullity:** Art. 3:41 BW applicable but rarely used.
- **Leading HR cases:** HR 11 december 2009, ECLI:NL:HR:2009:BK0461 — confirms interaction of art. 3:34 with burden of proof (**medium confidence**; verify precise pinpoint). Older: HR 18 december 1981 (under old BW) doctrine now superseded.
- **Remedies:** Vernietiging + restitution; counterparty protection via art. 3:35 BW (gerechtvaardigd vertrouwen) is **not** available against art. 3:34 once the stoornis is established and presumption of nadeel applies.
- **Cross-refs:** A1; A3 (wilsontbreken algemeen).

---

### A3. Wilsontbreken, schijnhandeling, simulatie
**RAG_TAG:** `nl.bw.3_33_35.wilsontbreken_simulatie`

- **Ground (NL/EN):** Ontbrekende wil / schijnhandeling / Lack of will / sham transaction.
- **Statutory anchor:** Art. 3:33 BW (wilsvertrouwensleer — a rechtshandeling requires a wil gericht op rechtsgevolg, uitgedrukt in een verklaring); art. 3:35 BW (protection of gerechtvaardigd vertrouwen of the counterparty).
- **Legal qualification:** **Nietig** if wil ontbreekt and art. 3:35 does not save the transaction; a pure schijnhandeling is nietig between parties but parties may be bound externally via art. 3:35 or 3:36 BW toward third parties.
- **Who can invoke:** Any party; rechter may treat it ambtshalve where openbare orde concerns arise, but normally on invocation.
- **Time limit:** None for nietigheid; verjaring of restitutory claims follows art. 3:306 et seq (20 years), or 3:309 BW (5 years for onverschuldigde betaling from bekendheid).
- **Partial nullity:** Yes, art. 3:41 BW.
- **Leading HR cases:** HR 11 juli 2008, ECLI:NL:HR:2008:BD1847 (confirmation of wilsvertrouwensleer; **medium confidence**). Classic illustrative case: simulated sale for tax purposes — no single canonical HR simulation case of the modern era dominates; flag "no single dominant leading HR case" and rely on Asser/Sieburgh 6-III.
- **Remedies:** Declaration of nietigheid; restitution; damages if counterparty acted in bad faith.
- **Cross-refs:** A4; C5 (bekrachtiging is not available for pure nietigheid — only conversie art. 3:42).

---

### A4. Vormgebrek — constitutief vs. bewijsvorm
**RAG_TAG:** `nl.bw.3_39.vormgebrek`

- **Ground (NL/EN):** Vormgebrek / Defect of form (constitutive vs. evidentiary).
- **Statutory anchor:** Art. 3:39 BW — "rechtshandelingen die niet in de voorgeschreven vorm zijn verricht, zijn nietig, tenzij uit de wet iets anders voortvloeit".
- **Legal qualification:** **Nietig** where the vorm is constitutief (e.g. notariële akte for overdracht onroerend goed art. 3:89 BW; huwelijkse voorwaarden art. 1:115 BW; testament art. 4:94 BW; schenking ter zake des doods art. 7:177 BW). Bewijsvorm (form required merely for evidence) does not trigger nietigheid — the rechtshandeling is valid but provability is constrained (e.g. art. 7:2 BW koop woning door particulier — nietig if not schriftelijk, which is **constitutief** for consumer home sales; contrast with art. 7A:1576i BW huurkoop registration, which is evidentiary).
- **Who can invoke:** Any party; the court can note nietigheid ambtshalve where form is of openbare orde (e.g. notariële akte requirements).
- **Time limit:** None for nietigheid itself; related restitutory claims are verjaarbaar under art. 3:306-310 BW.
- **Partial nullity:** Art. 3:41 BW — possible where the defect affects only one clause.
- **Leading HR cases:** HR 9 december 2011, ECLI:NL:HR:2011:BU7412 (art. 7:2 BW, consumer home purchase — schriftelijkheidsvereiste is constitutief; **verified** general line). HR 17 december 2004, ECLI:NL:HR:2004:AR1717 on vorm and gerechtvaardigd vertrouwen (**medium confidence** on pinpoint).
- **Remedies:** Declaration of nietigheid; conversie (art. 3:42 BW) sometimes available to rescue a defective act as a different valid act.
- **Cross-refs:** C4 (conversie).

---

### A5. Strijd met openbare orde of goede zeden
**RAG_TAG:** `nl.bw.3_40_1.openbare_orde_goede_zeden`

- **Ground (NL/EN):** Strijd met openbare orde of goede zeden / Contrary to public order or good morals.
- **Statutory anchor:** Art. 3:40 lid 1 BW.
- **Legal qualification:** **Nietig** (absolute nullity) — does not require invocation; works erga omnes.
- **Who can invoke:** Any party, any interested third party, and the rechter **ambtshalve** (this is recht van openbare orde).
- **Time limit:** None for nietigheid; restitution claims verjaarbaar (art. 3:309 BW, 5 years).
- **Partial nullity:** Yes, art. 3:41 BW — but only if the ongeldige part is severable without affecting the rest. Courts are stricter where the entire purpose is illicit.
- **Leading HR cases:**
  - **HR 1 juni 2012, ECLI:NL:HR:2012:BU5609 (Esmilo/Mediq Apotheken), NJ 2013/172 m.nt. T.F.E. Tjong Tjin Tai** — **verified**. Establishes the four-factor toetsingskader for when an agreement that obliges a verboden prestatie is nietig under art. 3:40 lid 1 BW: (i) welke belangen de geschonden regel beschermt, (ii) of door de inbreuk fundamentele beginselen worden geschonden, (iii) of partijen zich van de inbreuk bewust waren, (iv) of de regel in een sanctie voorziet. The mere fact that performance requires a statutory violation does not automatically render the contract nietig.
  - HR 7 april 2000, ECLI:NL:HR:2000:AA5401 (Parkeerexploitatie/Gemeente Amsterdam), NJ 2000/652 — **verified**; precursor to Esmilo/Mediq on strekking-toets.
  - HR 11 mei 2001, ECLI:NL:HR:2001:AB1555 (OZF/AZL), NJ 2002/364 — **verified**; further refinement.
- **Remedies:** Declaration of nietigheid; restitution via art. 6:203-211 BW; damages under 6:162 BW where the party invoking nullity is also culpable is generally **not** available (in pari delicto).
- **Cross-refs:** A6 (dwingende wet); C1 (strekking-toets); C2 (EU mandatory law).

---

### A6. Strijd met dwingende wetsbepaling (strekking-toets)
**RAG_TAG:** `nl.bw.3_40_2_3.dwingend_recht_strekkingstoets`

- **Ground (NL/EN):** Strijd met dwingende wetsbepaling / Violation of mandatory statutory rule.
- **Statutory anchor:** Art. 3:40 lid 2 BW (default: nietig if the wetsbepaling prohibits het verrichten of the rechtshandeling; vernietigbaar if the norm only protects one of the parties); art. 3:40 lid 3 BW (no effect on validity if the norm does not strekken tot aantasting of validity — the strekking-toets).
- **Legal qualification:** **Depends on strekking**:
  - Nietig (default under lid 2 first limb) where both parties are addressees.
  - Vernietigbaar where the norm is "uitsluitend strekt ter bescherming van een der partijen".
  - Geen gevolg voor geldigheid (lid 3) where the norm strekt niet tot aantasting.
- **Who can invoke:** Nietig → anyone + ambtshalve; vernietigbaar → only protected party (art. 3:50-52 BW).
- **Time limit:** Nietig: none. Vernietigbaar: 3 years under art. 3:52 BW.
- **Partial nullity:** Art. 3:41 BW — frequently applied, especially in complex commercial contracts where only one clause violates mandatory law (e.g. competition law, financial regulation).
- **Leading HR cases:**
  - **HR 1 juni 2012, ECLI:NL:HR:2012:BU5609 (Esmilo/Mediq), NJ 2013/172** — **verified**; strekking-toets doctrinal anchor (see A5).
  - HR 22 januari 1999, ECLI:NL:HR:1999:ZC2831 (Uneto/De Vliert), NJ 2000/305 — **medium confidence**; strekking-toets.
  - For EU-linked examples, see C2.
- **Remedies:** Nullity + restitution; or annulment + restitution; or no validity impact but possible damages under 6:162 BW.
- **Cross-refs:** A5; C1; C2.

---

### A7. Dwaling (art. 6:228 BW)
**RAG_TAG:** `nl.bw.6_228.dwaling`

- **Ground (NL/EN):** Dwaling / Mistake.
- **Statutory anchor:** Art. 6:228 BW. Four sub-types:
  - (a) **inlichtingendwaling** — lid 1 sub a: dwaling is het gevolg van een inlichting van de wederpartij;
  - (b) **schending mededelingsplicht** — lid 1 sub b: wederpartij had de dwalende behoren in te lichten;
  - (c) **wederzijdse dwaling** — lid 1 sub c: beide partijen van dezelfde onjuiste voorstelling zijn uitgegaan;
  - plus the limitation of lid 2: no vernietiging where the dwaling **uitsluitend een toekomstige omstandigheid** betreft, or in verband met de aard van de overeenkomst, de verkeersopvattingen of de omstandigheden van het geval voor rekening van de dwalende moet blijven.
- **Legal qualification:** **Vernietigbaar**.
- **Who can invoke:** Only the dwalende partij.
- **Time limit:** Art. 3:52 lid 1 sub c BW — three years from **ontdekking** of the dwaling.
- **Partial nullity:** Art. 3:41 BW applicable; in addition art. 6:230 BW allows **wijziging van de overeenkomst** by the court on request, as an alternative to vernietiging, to neutralise the nadeel.
- **Leading HR cases:**
  - **HR 15 november 1957, ECLI:NL:HR:1957:AG2023 (Baris/Riezenkamp), NJ 1958/67 m.nt. L.E.H. Rutten** — **verified**. Precontractual good-faith duty; counterparty may in beginsel rely on the wederpartij's statements; foundation for mededelingsplicht and for accepting dwaling as verweer without a separate vernietigingsactie.
  - **HR 21 december 1990, ECLI:NL:HR:1990:ZC0088 (Van Geest/Nederlof), NJ 1991/251** — **verified**. Mededelingsplicht generally prevails over onderzoeksplicht; protects even careless buyers.
  - **HR 10 april 1998, ECLI:NL:HR:1998:ZC2629 (Offringa/Vinck & Van Rosberg)** — **verified generally**; verhouding mededelings-/onderzoeksplicht bij onroerend goed.
  - HR 19 september 2003, ECLI:NL:HR:2003:AI0334 (Marks/Albert Schweitzer Ziekenhuis), NJ 2005/234 — **verified**; toepassing mededelingsplicht.
- **Remedies:** Vernietiging (ex tunc) + restitutie; OR wijziging overeenkomst (art. 6:230 BW); damages under art. 6:162/6:228 possible where mededelingsplicht schending tevens onrechtmatig is.
- **Cross-refs:** A8 (bedrog = aggravated inlichtingen/verzwijging + opzet); A10 (misbruik van omstandigheden).

---

### A8. Bedrog
**RAG_TAG:** `nl.bw.3_44_3.bedrog`

- **Ground (NL/EN):** Bedrog / Fraud (intentional misrepresentation).
- **Statutory anchor:** Art. 3:44 lid 3 BW — "bedrog is aanwezig, wanneer iemand een ander tot het verrichten van een bepaalde rechtshandeling beweegt door enige opzettelijk daartoe gedane onjuiste mededeling, door het opzettelijk daartoe verzwijgen van enig feit dat de verzwijger verplicht was mede te delen, of door een andere kunstgreep".
- **Legal qualification:** **Vernietigbaar**.
- **Who can invoke:** Only the misleide partij.
- **Time limit:** Art. 3:52 lid 1 sub c BW — three years from ontdekking van het bedrog.
- **Partial nullity:** Possible but unusual; typically the whole overeenkomst is tainted.
- **Leading HR cases:** HR 2 mei 1969 (Beukeboom/Van Dam) doctrinal origin (**LOW CONFIDENCE** on exact ECLI under old BW). Modern anchor: commentary rather than one dominant arrest. Flag: "no single dominant modern HR arrest; apply art. 3:44 lid 3 BW with Asser/Sieburgh 6-III commentary".
- **Remedies:** Vernietiging + restitutie + schadevergoeding onder 6:162 BW (bedrog is onrechtmatig).
- **Cross-refs:** A7; A9; A10.

---

### A9. Bedreiging
**RAG_TAG:** `nl.bw.3_44_2.bedreiging`

- **Ground (NL/EN):** Bedreiging / Duress.
- **Statutory anchor:** Art. 3:44 lid 2 BW.
- **Legal qualification:** **Vernietigbaar**.
- **Who can invoke:** Only the bedreigde partij. Art. 3:44 lid 5: bedreiging can be invoked even where the threat came from a third party, against a counterparty who had no knowledge, without the knowledge requirement applying (contrast bedrog/misbruik).
- **Time limit:** Art. 3:52 lid 1 sub b BW — three years after the bedreiging has ceased (note: this differs from bedrog/dwaling's "ontdekking" trigger).
- **Partial nullity:** Art. 3:41 BW in principle.
- **Leading HR cases:** No dominant modern HR arrest on art. 3:44 lid 2 BW pure bedreiging; older case law under the old BW is seldom cited. Flag: "no clear leading modern HR case".
- **Remedies:** Vernietiging + restitutie + schadevergoeding onder 6:162 BW.
- **Cross-refs:** A10.

---

### A10. Misbruik van omstandigheden
**RAG_TAG:** `nl.bw.3_44_4.misbruik_omstandigheden`

- **Ground (NL/EN):** Misbruik van omstandigheden / Abuse of circumstances (undue influence).
- **Statutory anchor:** Art. 3:44 lid 4 BW — requires: (i) bijzondere omstandigheden (noodtoestand, afhankelijkheid, lichtzinnigheid, abnormale geestestoestand, onervarenheid); (ii) de wederpartij weet of behoort te begrijpen dat dit de ander beweegt; (iii) bevordert niettemin de rechtshandeling.
- **Legal qualification:** **Vernietigbaar**.
- **Who can invoke:** Only the protected party.
- **Time limit:** Art. 3:52 lid 1 sub b BW — three years after the beïnvloedende bijzondere omstandigheid has ceased.
- **Partial nullity:** Possible; see also art. 3:54 BW — **wijziging ter opheffing van het nadeel** available as alternative (structurally similar to art. 6:230 BW at dwaling).
- **Leading HR cases:**
  - **HR 29 mei 1964, ECLI:NL:PHR:1964:AC4462 (Van Elmbt/Feierabend), NJ 1965/104 m.nt. G.J. Scholten** — **verified**. Holds that a specific measure or form of benadeling is not required; financial disadvantage is only one factor among many (aard van omstandigheden, wijze van gebruikmaking, verhouding partijen) that determine whether the overeenkomst is aangegaan "uit een oorzaak welke strijdt met de goede zeden".
  - **HR 27 januari 2017, ECLI:NL:HR:2017:95 (S'Energy/Delta), RvdW 2017/178** — **verified**. Benadeling is not a required element; it suffices that the invoker would not (or not on the same terms) have entered the contract absent the abuse.
- **Remedies:** Vernietiging OR wijziging (art. 3:54 BW) + schadevergoeding waar de gedraging ook onrechtmatig is.
- **Cross-refs:** A7; A8; A9.

---

### A11. Onbevoegde vertegenwoordiging + ultra vires rechtspersoon
**RAG_TAG:** `nl.bw.3_66_70.onbevoegde_vertegenwoordiging`

- **Ground (NL/EN):** Onbevoegde vertegenwoordiging; ultra vires / Unauthorized representation; ultra vires acts of legal persons.
- **Statutory anchor:** Arts. 3:66-3:70 BW (volmacht); art. 3:61 lid 2 BW (toerekenbare schijn); art. 2:7 BW (ultra vires — doeloverschrijding rechtspersoon).
- **Legal qualification:**
  - Onbevoegd verricht: **niet bindend voor de achterman**, absent bekrachtiging (art. 3:69 BW) of schijn van bevoegdheid (art. 3:61 lid 2 BW). Counterparty may hold the pseudo-volmacht giver liable under art. 3:70 BW.
  - Ultra vires (art. 2:7 BW): **vernietigbaar** op vordering van de rechtspersoon zelf, alleen indien de wederpartij de overschrijding kende of zonder eigen onderzoek moest kennen.
- **Who can invoke:**
  - Art. 3:66 onbevoegdheid: de achterman (pseudo-vertegenwoordigde).
  - Art. 2:7 ultra vires: **alleen de rechtspersoon** (protective nullity).
- **Time limit:** Art. 3:52 BW (three years) for ultra vires annulment; no fixed time limit for raising onbevoegdheid, but rechtsverwerking & art. 3:69 BW (termijnstelling by counterparty) apply.
- **Partial nullity:** Rarely relevant — usually the whole act is unattributable.
- **Leading HR cases:**
  - **HR 11 maart 1977, ECLI:NL:HR:1977:AC1877 (Kribbebijter), NJ 1977/521** — **verified**. The criterion for determining whether someone acted in eigen naam or as vertegenwoordiger depends on "hetgeen de betrokkenen daaromtrent jegens elkaar hebben verklaard en over en weer uit elkaars verklaringen en gedragingen hebben afgeleid en mochten afleiden".
  - **HR 19 februari 2010, ECLI:NL:HR:2010:BK7671 (ING/Bera), NJ 2010/115** — **verified**. Toerekenbare schijn mag worden gebaseerd op feiten en omstandigheden die voor risico van de achterman komen; risicoleer.
  - **HR 3 februari 2017, ECLI:NL:HR:2017:142 & ECLI:NL:HR:2017:143** — **verified**. Toerekenbare schijn mag niet uitsluitend op gedragingen van de onbevoegde vertegenwoordiger worden gebaseerd.
  - **HR 14 oktober 2022, ECLI:NL:HR:2022:1456 (Zilveren Kruis/IPGGZ)** — **verified**. Bevestigt dat toerekenbare schijn ook kan liggen in niet-doen / laten voortbestaan situatie.
- **Remedies:** Niet-gebondenheid achterman; schadevergoeding van pseudo-vertegenwoordiger ex art. 3:70 BW; bekrachtiging (art. 3:69 BW).
- **Cross-refs:** C5 (bekrachtiging); A3.

---

### A12. Ontbrekende toestemming echtgenoot / geregistreerd partner
**RAG_TAG:** `nl.bw.1_88_89.echtgenoot_toestemming`

- **Ground (NL/EN):** Ontbreken art. 1:88 BW-toestemming / Lack of spousal consent for certain protected acts.
- **Statutory anchor:** Art. 1:88 BW (categorieën: echtelijke woning, gift, borgtocht/medeschuldenaarschap buiten de normale uitoefening van beroep of bedrijf, koop op afbetaling); art. 1:89 BW (sanctie: vernietigbaarheid op vordering van de niet-toestemmende echtgenoot).
- **Legal qualification:** **Vernietigbaar**.
- **Who can invoke:** **Only the non-consenting echtgenoot/geregistreerd partner**, not the handelende echtgenoot, not the counterparty.
- **Time limit:** Art. 3:52 lid 1 sub d BW — three years after the niet-toestemmende echtgenoot ermee bekend is geworden.
- **Partial nullity:** Art. 3:41 BW applicable; in borgtochten frequently the entire borgtocht is vernietigd.
- **Leading HR cases:**
  - HR 13 juli 2007, ECLI:NL:HR:2007:BA7217 (Reinders Didam/Gunning q.q.) — **medium confidence**; art. 1:88 lid 5 BW (uitzondering voor normaal bedrijfsuitoefening door bestuurder/grootaandeelhouder).
  - HR 29 november 2002, ECLI:NL:HR:2002:AE8201 — **medium confidence**; toestemmingsvereiste bij borgtocht voor groepsvennootschap.
- **Remedies:** Vernietiging + restitutie; de niet-toestemmende echtgenoot kan buitengerechtelijk vernietigen (art. 3:49-50 BW).
- **Cross-refs:** None in this Part.

---

## PART B — UNFAIR TERMS & GENERAL CONDITIONS (afd. 6.5.3 BW + Richtlijn 93/13)

---

### B1. Onredelijk bezwarende bedingen — open norm
**RAG_TAG:** `nl.bw.6_233_a.onredelijk_bezwarend_open_norm`

- **Ground (NL/EN):** Onredelijk bezwarend beding in AV / Unreasonably onerous term in general conditions.
- **Statutory anchor:** Art. 6:233 aanhef en onder a BW — beding in AV is vernietigbaar indien, gelet op de aard en overige inhoud van de overeenkomst, wijze van totstandkoming, wederzijds kenbare belangen van partijen en overige omstandigheden, onredelijk bezwarend voor de wederpartij.
- **Legal qualification:** **Beding-niveau vernietigbaar** (het beding, niet de hele overeenkomst, tenzij art. 3:41 BW anders meebrengt).
- **Who can invoke:**
  - B2C (consument): elke wederpartij-consument; **rechter ambtshalve** verplicht (openbare orde via Richtlijn 93/13) — see B5.
  - B2B: alleen de wederpartij, geen ambtshalve toetsing; reflexwerking voor kleine ondernemers mogelijk in bijzondere omstandigheden (lagere rechtspraak).
  - Art. 6:235 BW sluit grote ondernemingen (balanstotaal/pers.) uit.
- **Time limit:** Art. 6:235 lid 4 BW — verjaringstermijn loopt niet zolang het beding niet is ingeroepen; voor de consument prevaleert richtlijn-conforme uitleg dat effectieve bescherming niet mag worden gefrustreerd door nationale verjaring (CJEU-Cofidis-lijn).
- **Partial nullity:** Ja; art. 3:41 BW. Voor consumentencontracten geldt de CJEU-regel: rechter mag oneerlijk beding niet matigen of herzien; hij moet het buiten toepassing laten (Banco Español de Crédito C-618/10), tenzij de overeenkomst dan onuitvoerbaar wordt en dit de consument zou benadelen (Kásler C-26/13).
- **Leading cases:**
  - **HR 13 september 2013, ECLI:NL:HR:2013:691 (Heesakkers/Voets), NJ 2014/274 m.nt. H.B. Krans** — **verified**. Ambtshalve toetsingsplicht art. 6:233 BW in consumentenovereenkomsten; regels zijn van openbare orde; rechter dient, zo nodig met instructiemaatregelen, oneerlijkheid te onderzoeken en beding bij oneerlijkheid te vernietigen.
  - **HR 29 april 2016, ECLI:NL:HR:2016:769 (SEBA/Amsterdam)** — **verified**. Bij de oneerlijkheidstoets mag geen rekening worden gehouden met art. 6:248 lid 2 BW — het beding als zodanig wordt getoetst.
  - **HR 28 september 2018, ECLI:NL:HR:2018:1800, NJ 2020/68** — **verified**. Maatstaf: vergelijking met default nationaal recht om "aanzienlijke verstoring van het evenwicht" vast te stellen.
- **Remedies:** Vernietiging van het beding; overeenkomst blijft voor het overige in stand (art. 3:41 BW / art. 6 Richtlijn 93/13).
- **Cross-refs:** B2; B3; B4; B5.

---

### B2. Zwarte lijst — art. 6:236 BW
**RAG_TAG:** `nl.bw.6_236.zwarte_lijst_b2c`

- **Ground (NL/EN):** Zwarte lijst / "Black list" — per se onredelijk bezwarende bedingen jegens consumenten.
- **Statutory anchor:** Art. 6:236 BW (bij B2C). Onverkort **vernietigbaar** per definitie; geen nadere toets. Categorieën (sub a–n, huidige tekst): uitsluiten recht op nakoming (a); beroven recht op ontbinding (b); uitsluiten/beperken ontbindings- of schorsingsrecht (c); onbepaalde termijn-bevoegdheid gebruiker (d); onredelijke verlenging (e/j); rechterlijke verklaringsbinding (e) en uitsluiting van rechtsmiddelen (n) in arbitrage, enz. Exacte sub-enumeratie: **raadpleeg actuele tekst wetten.overheid.nl** — de lijst is meermalen aangevuld (art. 6:236 onder l t/m o toegevoegd via Wet Implementatie Consumentenrichtlijnen en Richtlijn 2011/83/EU).
- **Legal qualification:** **Vernietigbaar per se** (geen belangenafweging).
- **Who can invoke:** Consument-wederpartij; rechter ambtshalve.
- **Time limit:** Zie B1 + art. 6:235 lid 4 BW.
- **Partial nullity:** Beding wordt geschrapt; overeenkomst blijft overig in stand.
- **Leading cases:** Toepassing via Heesakkers/Voets (B1) en Dexia-lijn (HR 21 april 2017, ECLI:NL:HR:2017:773 — **verified**; art. 6 Bijzondere Voorwaarden Dexia oneerlijk, niet te matigen).
- **Remedies:** Vernietiging van het beding; bij vervolg schadevergoeding uit art. 6:277 BW (zie Dexia 2017).
- **Cross-refs:** B1; B3; B5.

---

### B3. Grijze lijst — art. 6:237 BW
**RAG_TAG:** `nl.bw.6_237.grijze_lijst_b2c`

- **Ground (NL/EN):** Grijze lijst / "Grey list" — vermoedens van onredelijke bezwaarlijkheid.
- **Statutory anchor:** Art. 6:237 BW. Opsomming van bedingen die **worden vermoed** onredelijk bezwarend te zijn; de gebruiker moet het vermoeden weerleggen. Categorieën omvatten o.a. onredelijke boete-, rente-, opzegtermijn-, exoneratie-, rechtskeuze- en rechtsverwerkingsbedingen. Exacte lijst: **raadpleeg wetten.overheid.nl**.
- **Legal qualification:** **Vernietigbaar** tenzij gebruiker het vermoeden succesvol weerlegt.
- **Who can invoke:** Consument; rechter ambtshalve.
- **Time limit:** Zie B1.
- **Partial nullity:** Ja; beding geschrapt.
- **Leading cases:** HR 22 november 2019, ECLI:NL:HR:2019:1830 (ABN AMRO / rentewijzigingsbeding hypotheek) — **verified**; transparantie + evenwicht + bijlage Richtlijn bij grijze lijst-achtige wijzigingsbedingen.
- **Remedies:** Vernietiging.
- **Cross-refs:** B1; B2; B5.

---

### B4. Toepasselijkheid & kennisnemingsmogelijkheid
**RAG_TAG:** `nl.bw.6_233_b_234.av_toepasselijkheid`

- **Ground (NL/EN):** Toepasselijkheid AV niet overeengekomen / geen redelijke kennisnemingsmogelijkheid / AV not applicable or not made reasonably available.
- **Statutory anchor:** Art. 6:233 sub b BW + art. 6:234 BW (ter handstelling voor of bij het sluiten van de overeenkomst, of electronische terbeschikkingstelling indien overeenkomst elektronisch).
- **Legal qualification:** **Vernietigbaar** voor het beding waarnaar wordt verwezen (niet de AV als geheel in abstracto, maar de bedingen die men wil inroepen).
- **Who can invoke:** Wederpartij (B2C én B2B binnen toepassingsbereik art. 6:235 BW).
- **Time limit:** Zie B1.
- **Partial nullity:** Per beding.
- **Leading cases:**
  - HR 1 oktober 1999, ECLI:NL:HR:1999:ZC2977 (Geurtzen/Kampstaal), NJ 2000/207 — **verified**. Ruimere uitleg van terhandstelling: ook als de wederpartij kenbaar reeds op de hoogte was.
  - HR 11 februari 2011, ECLI:NL:HR:2011:BO7108 (First Data/KPN), NJ 2011/571 — **verified**. Electronische terbeschikkingstelling bij elektronische contracten toegelaten.
- **Remedies:** Vernietiging van het beding; AV blijven voor de rest buiten toepassing.
- **Cross-refs:** B1.

---

### B5. Ambtshalve toetsing — Richtlijn 93/13/EEG
**RAG_TAG:** `eu.rl_93_13.ambtshalve_toetsing_consument`

- **Ground (NL/EN):** Ambtshalve toetsing oneerlijke bedingen (consumentenrecht) / Ex officio review of unfair consumer terms.
- **Statutory anchor:** Richtlijn 93/13/EEG (arts. 3, 4, 6, 7); art. 6 lid 1: oneerlijke bedingen **niet-bindend**. Geïmplementeerd in Nederland via richtlijn-conforme uitleg van art. 6:233 BW e.v.
- **Legal qualification:** **Niet-bindend** (richtlijn-terminologie) → in Nederland vormgegeven als **vernietigbaar**, maar met ambtshalve plicht van de rechter en zonder verjaringsbarrière waar die de effectieve bescherming van de consument frustreert (CJEU Cofidis C-473/00).
- **Who can invoke:** Consument + **rechter ambtshalve verplicht** zodra hij over feitelijke en juridische gegevens beschikt (Pannon GSM C-243/08).
- **Time limit:** Effectiviteitsbeginsel — nationale termijnen mogen de effectieve bescherming niet frustreren.
- **Partial nullity:** Ja; CJEU Banco Español C-618/10: rechter mag het oneerlijke beding niet matigen, slechts buiten toepassing laten; uitzondering: indien overeenkomst anders niet in stand kan blijven en dit juist voor de consument nadelig is (Kásler C-26/13).
- **Leading cases:**
  - CJEU: **Océano Grupo C-240/98**; **Pannon GSM C-243/08**; **Mostaza Claro C-168/05**; **Asturcom C-40/08**; **VB Pénzügyi Lízing C-137/08** (NJ 2011/41); **Banco Español de Crédito C-618/10** (NJ 2012/512); **Aziz C-415/11**; **Kásler C-26/13**; **Radlinger C-377/14**; **Asbeek Brusse C-488/11**; arresten 17 mei 2022 (C-600/19, C-693/19, C-725/19, C-869/19).
  - **HR 13 september 2013, ECLI:NL:HR:2013:691 (Heesakkers/Voets), NJ 2014/274** — **verified** (see B1).
  - **HR 26 februari 2016, ECLI:NL:HR:2016:340, NJ 2017/214** — **verified**. Verduidelijking ambtshalve toetsing in appel; grenzen rechtsstrijd versus openbare orde.
  - **HR 21 april 2017, ECLI:NL:HR:2017:773 (Dexia)** — **verified**. Toepassing oneerlijkheidstoets op effectenleaseclausules.
  - **HR 22 november 2019, ECLI:NL:HR:2019:1830 (ABN AMRO hypotheekrente-beding)** — **verified**.
  - **HR 24 november 2023, ECLI:NL:HR:2023:1627** — **verified**. Prejudiciële beslissing: wettelijke verzettermijn geldt ook als ambtshalve toetsing ten onrechte is nagelaten.
- **Remedies:** Beding buiten toepassing; geen matiging; uitkomst via default recht (o.a. 6:277 BW bij contractuele rente).
- **Cross-refs:** B1; B2; B3.

---

## PART C — PERFORMANCE & TIME-LIMIT GROUNDS

---

### C1. Onmogelijkheid van de prestatie
**RAG_TAG:** `nl.bw.6_74_227.onmogelijkheid_prestatie`

- **Ground (NL/EN):** Onmogelijkheid / Impossibility of performance.
- **Statutory anchor:**
  - Initiële onmogelijkheid / onbepaalbaarheid: art. 6:227 BW (verbintenissen moeten bepaalbaar zijn); echter soepel uitgelegd — de verbintenissen kunnen achteraf worden vastgesteld aan de hand van tevoren vaststaande criteria of redelijkheid en billijkheid.
  - Subsequent onmogelijkheid / overmacht: arts. 6:74, 6:75 BW (overmacht), 6:265 BW (ontbinding).
- **Legal qualification:**
  - Initieel onbepaalbaar: **nietig** (ontstaat geen verbintenis).
  - Subsequente onmogelijkheid: overeenkomst is **geldig**; de prestatie is niet-afdwingbaar en de wanprestatie kan tot ontbinding/schadevergoeding leiden tenzij overmacht de toerekening uitsluit.
- **Who can invoke:** Elke partij; rechter past toe binnen grenzen van de rechtsstrijd.
- **Time limit:** Geen voor de initiële nietigheid zelf; ontbindings-/schadevergoedingsactie verjaart onder art. 3:307-311 BW.
- **Partial nullity:** Art. 3:41 BW voor het onbepaalbare deel.
- **Leading cases:**
  - HR 2 februari 2018, ECLI:NL:HR:2018:148 — **medium confidence**; bepaalbaarheid onder 6:227 BW, soepele toets via 6:248 BW.
  - HR 17 juni 2005, ECLI:NL:HR:2005:AT1437 — **medium confidence**; verkoopprijs bepaalbaar via criteria.
  - Geen dominant klassiek arrest; verwijs naar Asser/Hartkamp 6-III over bepaalbaarheid.
- **Remedies:** Nietigheid (initiëel); bij subsequente onmogelijkheid: ontbinding (6:265), schadevergoeding (6:74), ontheffing bij overmacht (6:75).
- **Cross-refs:** C2.

---

### C2. Onvoorziene omstandigheden (hardship)
**RAG_TAG:** `nl.bw.6_258.onvoorziene_omstandigheden`

- **Ground (NL/EN):** Onvoorziene omstandigheden / Unforeseen circumstances — hardship.
- **Statutory anchor:** Art. 6:258 BW (dwingend recht per art. 6:250 BW); art. 6:260 BW (rechter kan voorwaarden stellen bij wijziging/ontbinding).
- **Legal qualification:** **Enforceability modifier, not a validity ground**. Rechter kan op vordering van een partij de gevolgen wijzigen of de overeenkomst (ged.) ontbinden.
- **Who can invoke:** Partij; géén ambtshalve toepassing (art. 6:258 lid 1 BW vereist een "vordering").
- **Time limit:** Normale verjaringstermijnen — maar de doctrine vereist dat de omstandigheid toekomstig moet zijn ten opzichte van het sluitmoment (Briljant Schreuders/ABP).
- **Partial nullity:** N.v.t.; wel gedeeltelijke ontbinding mogelijk.
- **Leading cases:**
  - **HR 20 februari 1998, ECLI:NL:HR:1998:ZC2587 (Briljant Schreuders/ABP), NJ 1998/493** — **verified**. Onvoorziene omstandigheden alleen voor omstandigheden die ten tijde van sluiting nog in de toekomst lagen; rechter moet terughoudend zijn; redelijkheid en billijkheid verlangen in de eerste plaats trouw aan het gegeven woord.
  - HR 19 november 1993, ECLI:NL:HR:1993:ZC1152 (Campina/Van Jole), NJ 1994/156 — **verified**; terughoudendheid rechter.
  - HR 25 juni 1999, ECLI:NL:HR:1999:AD3069 (VvdE/CSM), NJ 1999/602 — **verified**; samenloop met 6:248 BW bij duurovereenkomsten.
  - HR 13 oktober 2017, ECLI:NL:HR:2017:2615 — **medium confidence**; recente toepassing.
- **Remedies:** Wijziging overeenkomst / (ged.) ontbinding; rechter kan voorwaarden stellen (6:260 BW).
- **Cross-refs:** C1; A7 (samenloop met dwaling bij omstandigheden aanwezig ten tijde van contractsluiting).

---

### C3. Klachtplicht / protestplicht
**RAG_TAG:** `nl.bw.6_89_7_23.klachtplicht`

- **Ground (NL/EN):** Klachtplicht (art. 6:89 BW) / koopklachtplicht (art. 7:23 BW) / Duty to complain in timely fashion.
- **Statutory anchor:** Art. 6:89 BW (algemeen: schuldeiser moet binnen bekwame tijd na ontdekking protesteren); art. 7:23 BW (koop — lex specialis; 2 maanden consumentenkoop).
- **Legal qualification:** **Procedureel niet-afdwingbaar / rechtsverval**. De overeenkomst is geldig maar alle remedies (nakoming, ontbinding, schadevergoeding, **en dwaling**) vervallen.
- **Who can invoke:** Schuldenaar, als verweer. Art. 6:89 BW mag **niet ambtshalve** worden toegepast (HR 20 januari 2006, ECLI:NL:HR:2006:AU4122, NJ 2006/80 — verified).
- **Time limit:** "Binnen bekwame tijd" — contextueel; géén starre termijn. Consumentenkoop: 2 maanden is in elk geval tijdig (7:23 lid 1 slot).
- **Partial nullity:** N.v.t.
- **Leading cases:**
  - **HR 29 juni 2007, ECLI:NL:HR:2007:AZ7617 (Pouw/Visser), NJ 2008/606 m.nt. Jac. Hijma** — **verified**. Geen starre termijn; afhankelijk van alle omstandigheden; onderzoeks- en mededelingsplicht voor koper; nadeel schuldenaar als factor.
  - **HR 25 maart 2011, ECLI:NL:HR:2011:BP8991 (Ploum/Smeets II)** — **verified**. Nadeelsvereiste zwaardere weging.
  - **HR 8 februari 2013, ECLI:NL:HR:2013:BY4600 (Van de Steeg/Rabobank), NJ 2014/497** — **verified**. Belangenafweging tussen tijdsverloop en benadeling schuldenaar; "alles-of-niets"-benadering getemperd.
  - **HR 8 oktober 2010, ECLI:NL:HR:2010:BM9615 (Tan/Forward / "Lafranca")** — **verified (ECLI only; label varies)**. Bekwame tijd 6:89 BW sterk casuïstisch.
  - HR 23 maart 2007, ECLI:NL:HR:2007:AZ3531 (Brocacef/Simons), NJ 2007/176 — **verified**. Art. 6:89 BW geldt niet bij algeheel niet-presteren.
- **Remedies:** Geen — verval van alle remedies uit de tekortkoming (nakoming, ontbinding, schadevergoeding, prijsvermindering, dwaling). Uitzondering: parallelle vordering uit onrechtmatige daad op niet-identieke feiten blijft mogelijk (HR 2017:2902 — medium confidence).
- **Cross-refs:** A7; C4.

---

### C4. Verjaring — algemeen regime
**RAG_TAG:** `nl.bw.3_306_325.verjaring`

- **Ground (NL/EN):** Verjaring / Statute of limitations.
- **Statutory anchor:** Arts. 3:306-3:325 BW. Kernregels:
  - Art. 3:306 BW: **20 jaar** absoluut (restcategorie).
  - Art. 3:307 BW: **5 jaar** vordering tot nakoming verbintenis uit overeenkomst — begint na opeisbaarheid.
  - Art. 3:308 BW: **5 jaar** periodieke betalingen (rente/huur/loon) — vanaf opeisbaarheid elke termijn.
  - Art. 3:309 BW: **5 jaar** onverschuldigde betaling — vanaf bekendheid schuldeiser én debiteur; uiterlijk 20 jaar.
  - Art. 3:310 BW: **5 jaar** vordering schadevergoeding — vanaf bekendheid schade én aansprakelijke persoon; uiterlijk 20 jaar (bij letsel/verontreiniging tot 30 jaar/geen absolute termijn bij personenschade).
  - Art. 3:311 BW: **5 jaar** ontbinding/herstel bij tekortkoming — vanaf bekendheid.
  - Art. 3:316-319 BW: stuiting (schriftelijke aanmaning + gerechtelijke/buitengerechtelijke handelingen).
  - Art. 3:320-321 BW: verlenging in bijzondere relaties (echtgenoten, ouders/kinderen, curator/onder curatele gestelden).
  - Art. 3:322 BW: verjaring moet worden ingeroepen; **niet ambtshalve** door rechter.
- **Legal qualification:** **Niet-afdwingbaar na verjaring** (vordering blijft als natuurlijke verbintenis bestaan — art. 6:3 lid 2 sub a BW).
- **Who can invoke:** Schuldenaar, als verweer. **Niet ambtshalve** (art. 3:322 lid 1 BW).
- **Time limit:** Zie boven.
- **Partial nullity:** N.v.t.
- **Leading cases:**
  - **HR 31 oktober 2003, ECLI:NL:HR:2003:AL8168 (Saelman), NJ 2006/112** — **verified**. Korte verjaring 3:310 BW begint pas bij daadwerkelijke bekendheid met schade én aansprakelijke persoon (subjectieve maatstaf).
  - **HR 28 april 2000, ECLI:NL:HR:2000:AA5635 (Van Hese/De Schelde), NJ 2000/430** — **verified**. Lange 30-jaarstermijn kan in uitzonderlijke gevallen (asbest/mesothelioom) op grond van 6:2 lid 2 BW buiten toepassing blijven.
  - HR 4 mei 2018, ECLI:NL:HR:2018:677 — **medium confidence**; stuiting-maatstaf bij verwijzing naar eerdere aansprakelijkstelling.
- **Remedies:** Verval van afdwingbaarheid (natuurlijke verbintenis blijft).
- **Cross-refs:** C3; C5.

---

### C5. Vervaltermijnen (contractueel & statutair)
**RAG_TAG:** `nl.bw.vervaltermijnen`

- **Ground (NL/EN):** Vervaltermijnen / Forfeiture periods.
- **Statutory anchor:** Geen algemene regel; verspreid (bv. art. 7:23 lid 2 BW; art. 6:191 BW productaansprakelijkheid; art. 1:89 BW toestemming echtgenoot via 3:52; diverse arbeidsrechtelijke termijnen in 7:677-686a BW; art. 1020 e.v. Rv arbitrageverzoeken).
- **Legal qualification:** Bij verval: **recht gaat teniet van rechtswege** (anders dan verjaring). **Ambtshalve** toe te passen waar van openbare orde; geen stuiting; geen verlenging tenzij wet anders bepaalt.
- **Who can invoke:** Elke partij + rechter ambtshalve (meestal).
- **Time limit:** Per bepaling.
- **Partial nullity:** N.v.t.
- **Leading cases:** HR 11 september 2020, ECLI:NL:HR:2020:1413 — **medium confidence**; onderscheid verval/verjaring. Reguliere toepassing via 7:23 BW-jurisprudentie (C3).
- **Remedies:** Verval recht.
- **Cross-refs:** C3; C4.

---

## PART D — PROCEDURAL & CROSS-BORDER ENFORCEABILITY

---

### D1. Arbitragebeding — ongeldigheid / niet-arbitrabel / vormgebrek
**RAG_TAG:** `nl.rv.1020_1023.arbitrage`

- **Ground (NL/EN):** Arbitragebeding niet-afdwingbaar / Arbitration clause unenforceable.
- **Statutory anchor:** Arts. 1020-1023 Rv; art. 1021 Rv (schriftelijkheidsvereiste: vastlegging in geschrift, niet per se ondertekend); art. 1020 lid 3 Rv (**niet arbitrabel**: "rechtsgevolgen die niet ter vrije bepaling van partijen staan" — o.a. de status personarum, ontbinding huwelijk, personenrechtelijke kwesties); art. 1065 Rv (vernietigingsgronden).
- **Legal qualification:**
  - Geen geldige overeenkomst: arbitrage onbevoegd; rechter is bevoegd.
  - B2C: arbitragebeding dat de consument verplicht zonder keuze is op de zwarte lijst (art. 6:236 sub n BW — **verified als current law na Wet modernisering arbitragerecht 2015**).
  - Niet-arbitrabel onderwerp (1020 lid 3 Rv): arbitragebeding mist effect voor die categorie.
- **Who can invoke:** Elke partij (via onbevoegdheidsverweer of 1065 Rv vernietigingsactie); ambtshalve bij niet-arbitrabel onderwerp en bij oneerlijke bedingen jegens consument (CJEU Mostaza Claro C-168/05; Asturcom C-40/08).
- **Time limit:** Art. 1064 Rv: drie maanden voor vernietigingsvordering tegen arbitraal vonnis.
- **Partial nullity:** Ja; oneerlijk beding wordt buiten toepassing gelaten.
- **Leading cases:**
  - **CJEU Mostaza Claro C-168/05** — **verified**. Ambtshalve toetsing oneerlijkheid arbitragebeding in vernietigingsprocedure.
  - **CJEU Asturcom C-40/08** — **verified**. Ambtshalve toetsing ook in exequatur.
  - Pre-2015 HR-lijn over consumentenarbitrage: HR 21 september 2012, ECLI:NL:HR:2012:BW6135 — **medium confidence**; relevantie ondermijnd door wetswijziging 2015 en art. 6:236 sub n BW.
- **Remedies:** Onbevoegdheid arbiter; vernietiging arbitraal vonnis (1065 Rv); weigering exequatur voor oneerlijk beding.
- **Cross-refs:** B2; B5.

---

### D2. Forumkeuze — Brussel I-bis + Rv
**RAG_TAG:** `eu.vo_1215_2012.forumkeuze`

- **Ground (NL/EN):** Forumkeuzebeding onwerkzaam / Choice-of-court clause unenforceable.
- **Statutory anchor:**
  - EU: Vo. 1215/2012 (Brussel I-bis) arts. 25 (formvereisten en materiële geldigheid naar recht aangewezen rechtbank), 26 (stilzwijgende forumkeuze), 17-19 (consument), 20-23 (werknemer), 10-16 (verzekerden) — forumkeuzen jegens deze zwakke partijen zijn beperkt geldig (meestal alleen ná geschil).
  - Nationaal (buiten EU-toepassingsgebied): arts. 8, 108 Rv.
- **Legal qualification:** **Procedureel niet-afdwingbaar** bij schending beschermingsregels zwakke partijen of formgebrek; rechter die anders bevoegd zou zijn, blijft bevoegd.
- **Who can invoke:** Elke partij; rechter ambtshalve bij verzekerings-/consumenten-/arbeidszaken binnen EU-regime.
- **Time limit:** Forumverweer moet tijdig worden gevoerd (voor verweer ten gronde); zie ook art. 26 Brussel I-bis (stilzwijgende aanvaarding).
- **Partial nullity:** Beding geschrapt, overeenkomst blijft in stand.
- **Leading cases:**
  - **CJEU El Majdoub C-322/14** — **verified**. Click-wrap accepteerbaar als "schriftelijk" onder art. 25.
  - **CJEU Höszig C-222/15** — **verified**. Algemene voorwaarden + forumkeuze; bepaaldheidsvereiste.
  - CJEU Powell Duffryn C-214/89 — **verified**. Forumkeuze in statuten NV bindt aandeelhouders.
  - HR-rechtspraak toepassing: HR 18 september 2020, ECLI:NL:HR:2020:1443 — **medium confidence**; wilsovereenstemming forumkeuze.
- **Remedies:** Onbevoegdheidsverklaring van gekozen forum óf weigering van exequatur.
- **Cross-refs:** D3.

---

### D3. Rechtskeuze & voorrangsregels — Rome I
**RAG_TAG:** `eu.vo_593_2008.rome_i_rechtskeuze`

- **Ground (NL/EN):** Rechtskeuze onwerkzaam of beperkt / overriding mandatory rules / Choice-of-law unenforceable in whole or part.
- **Statutory anchor:** Vo. 593/2008 (Rome I): art. 3 (vrije rechtskeuze); art. 3 lid 3 (zuiver interne situaties — dwingende regels van dat land blijven van toepassing); art. 6 (consumentencontracten — niet-wegcontracteerbare beschermingsregels van het gewone verblijfsrecht van de consument); art. 8 (individuele arbeidsovereenkomst — recht dat zonder keuze zou gelden, voor zover gunstiger); art. 9 (voorrangsregels — overriding mandatory provisions); art. 21 (openbare orde uitzondering).
- **Legal qualification:** Rechtskeuze is **geldig**, maar de aanwijzing is **niet-afdwingbaar** voor zover (a) het dwingende recht van het "normaal toepasselijk" recht de zwakke partij beter beschermt, (b) voorrangsregels van de forum- of nauw betrokken staat ingrijpen, (c) openbare orde van het forum in de weg staat.
- **Who can invoke:** Partij; rechter ambtshalve bij openbare orde en bij consumentendwingend recht in de lijn van de ambtshalve toetsingsplicht.
- **Time limit:** N.v.t.
- **Leading cases:**
  - **CJEU Unamar C-184/12** — **verified**. Toepassing art. 9 Rome I op handelsagenten; voorrangsregels.
  - **CJEU Nikiforidis C-135/15** — **verified**. Art. 9 lid 3 Rome I beperkt uitwerking voorrangsregels derde staten.
- **Remedies:** Parallelle toepassing gunstigere dwingende regels; weigering toepassing gekozen recht voor zover in strijd met voorrangsregels/openbare orde.
- **Cross-refs:** D2.

---

### D4. Pauliana — faillissementsrechtelijk
**RAG_TAG:** `nl.fw.42_47.faillissementspauliana`

- **Ground (NL/EN):** Faillissementspauliana / Insolvency clawback.
- **Statutory anchor:** Arts. 42-51 Fw.
  - Art. 42 Fw: **onverplichte rechtshandelingen** — vernietigbaar bij benadeling schuldeisers + wetenschap van benadeling bij schuldenaar én wederpartij (bij onder bezwarende titel) of bij schuldenaar alleen (om niet).
  - Art. 43 Fw: **bewijsvermoedens** bij bepaalde rechtshandelingen binnen één jaar voor faillissement (o.a. zekerheidsstelling voor oude schuld, niet-opeisbare schulden, verbonden personen).
  - Art. 45 Fw: om-niet-handelingen binnen één jaar — bewijsvermoeden benadeling + wetenschap aan zijde schuldenaar.
  - Art. 47 Fw: **verplichte rechtshandelingen** (voldoening opeisbare schuld) — alleen vernietigbaar bij samenspanning of wetenschap van faillissementsaanvraag.
- **Legal qualification:** **Vernietigbaar** door curator (art. 42-49 Fw).
- **Who can invoke:** Uitsluitend de **curator** (art. 49 Fw).
- **Time limit:** Art. 3:52 BW analoog — drie jaar na het verrichten van de rechtshandeling / na bekendwording curator; faillissementsopeningstijd relevant.
- **Partial nullity:** Ja, voor zover vereist om de benadeling op te heffen (art. 51 Fw-restitutie).
- **Leading cases:**
  - **HR 16 juni 2000, ECLI:NL:HR:2000:AA6234 (Van Dooren q.q./ABN AMRO I), NJ 2000/578** — **verified**. Restrictieve uitleg art. 47 Fw; "wetenschap" + "samenspanning".
  - **HR 8 juli 2005, ECLI:NL:HR:2005:AT1089 (Van Dooren q.q./ABN AMRO II), NJ 2005/457 m.nt. P. van Schilfgaarde** — **verified**. Maatstaf wetenschap van benadeling; berekening benadeling.
  - **HR 22 december 2009, ECLI:NL:HR:2009:BI8493 (ABN AMRO/Van Dooren q.q. III), NJ 2010/273** — **verified**. Kern-maatstaf: wetenschap van benadeling ex art. 42 Fw aanwezig als ten tijde van de handeling "het faillissement en een tekort daarin met een redelijke mate van waarschijnlijkheid waren te voorzien" voor zowel schuldenaar als wederpartij — ook in reddingsoperaties.
  - HR 1 oktober 1993, ECLI:NL:HR:1993:ZC1081 (Ontvanger/Pelicaan), NJ 1994/257 — **verified**; wetenschap van werkelijke benadeling, niet slechts kans.
- **Remedies:** Vernietiging jegens boedel; restitutie goederen/waarde aan boedel (art. 51 Fw); wederpartij wordt concurrent crediteur voor eigen prestatie.
- **Cross-refs:** D5.

---

### D5. Pauliana — buiten faillissement
**RAG_TAG:** `nl.bw.3_45_48.pauliana_buiten_faillissement`

- **Ground (NL/EN):** Actio Pauliana buiten faillissement.
- **Statutory anchor:** Arts. 3:45-3:48 BW.
  - 3:45 lid 1: onverplichte rechtshandeling vernietigbaar door benadeelde schuldeiser bij benadeling + wetenschap bij schuldenaar (+ wederpartij indien onder bezwarende titel).
  - 3:46: vermoedens van wetenschap (analog aan 43 Fw) bij handelingen binnen 1 jaar; verbonden personen.
  - 3:47: om niet — benadeling vermoed.
  - 3:48: vergeefse uitwinning niet vereist; het volstaat dat schuldeiser benadeeld wordt.
- **Legal qualification:** **Vernietigbaar** (relatief) — werkt alleen voor de inroepende schuldeiser (art. 3:45 lid 4 BW).
- **Who can invoke:** De benadeelde schuldeiser zelf.
- **Time limit:** Art. 3:52 lid 1 sub c BW — drie jaar na ontdekking van de benadeling.
- **Partial nullity:** Ja, voor zover vereist (art. 3:45 lid 4 BW).
- **Leading cases:**
  - HR 26 augustus 2003, ECLI:NL:HR:2003:AF8540, NJ 2004/549 — **verified generally**; wetenschap van benadeling — kans is onvoldoende.
  - HR 1 juli 2005, ECLI:NL:HR:2005:AT3668 — **medium confidence**; benadelingsmaatstaf.
- **Remedies:** Vernietiging relatief jegens inroepende schuldeiser; herstel verhaalspositie.
- **Cross-refs:** D4.

---

### D6. Beslagverboden en executiebeperkingen
**RAG_TAG:** `nl.rv.beslagverboden_executiebeperkingen`

- **Ground (NL/EN):** Beslagverboden en executiebeperkingen / Attachment prohibitions and execution limits.
- **Statutory anchor:**
  - Arts. 447-448 Rv: onvatbaar voor beslag (o.a. bed, kleding, voor beroep/studie onmisbare zaken, huisdieren van niet-commerciële aard, eten voor één maand).
  - Arts. 475a-475g Rv: **beslagvrije voet** bij beslag op loon, uitkering, pensioen; herberekend na Wet vereenvoudiging beslagvrije voet 2021.
  - Art. 436 Rv: onvatbaar voor beslag zijn vorderingen die bij de wet onvatbaar zijn verklaard (bv. bepaalde uitkeringen).
  - Art. 479kk-479pa Rv: speciaal regime pensioenrechten / alimentatie.
  - Art. 3:276 BW: uitgangspunt verhaal op alle vermogen **tenzij de wet of de overeenkomst anders bepaalt**.
- **Legal qualification:** **Procedureel niet-afdwingbaar** — veroordelingstitel blijft geldig, maar bepaalde goederen zijn onvatbaar voor beslag/executie.
- **Who can invoke:** Schuldenaar/derde; deurwaarder dient ambtshalve te respecteren (bij consumentenbeslag); rechter toetst in executiegeschil (art. 438 Rv).
- **Time limit:** N.v.t.
- **Partial nullity:** N.v.t.
- **Leading cases:**
  - HR 31 oktober 2014, ECLI:NL:HR:2014:3068 — **medium confidence**; uitleg 475a Rv (beslagvrije voet).
  - Geen dominant HR-arrest modern; kern is wettelijk.
- **Remedies:** Opheffing beslag via kort geding (705 Rv); executiegeschil (438 Rv).
- **Cross-refs:** None.

---

## PART E — CROSS-CUTTING DOCTRINAL OVERLAYS

---

### E1. Strekking-toets onder art. 3:40 lid 2 BW
**RAG_TAG:** `nl.bw.3_40_2.strekkingstoets_doctrine`

- **Doctrine:** Bij strijd met een dwingende wetsbepaling bepaalt art. 3:40 lid 2-3 BW welk rechtsgevolg volgt: nietig, vernietigbaar, of geen gevolg. Kritische variabele is de **strekking** van de geschonden norm.
- **Function:** Validity gate voor rechtshandelingen die een dwingende wetsbepaling schenden.
- **Toets / criteria:**
  1. Schendt de rechtshandeling een norm waarvan het verrichten (niet de inhoud/strekking van de prestatie) door de wet is verboden? → lid 2, default nietig.
  2. Strekt de norm **uitsluitend tot bescherming van één partij**? → vernietigbaar.
  3. Strekt de norm **niet** tot aantasting van de geldigheid? → lid 3, géén invaliditeitsgevolg.
  4. Raakt het de inhoud/strekking van de prestatie (niet het verrichten)? → lid 1 openbare orde-toets, vier Esmilo/Mediq-factoren (belangen; fundamentele beginselen; bewustheid partijen; sanctiesysteem).
- **Leading cases:**
  - **HR 1 juni 2012, ECLI:NL:HR:2012:BU5609 (Esmilo/Mediq), NJ 2013/172** — **verified**. Vier-factoren-toets; nietigheid niet automatisch bij verboden prestatie.
  - HR 7 april 2000, ECLI:NL:HR:2000:AA5401 (Parkeerexploitatie/Amsterdam), NJ 2000/652 — **verified**.
  - HR 11 mei 2001, ECLI:NL:HR:2001:AB1555 (OZF/AZL), NJ 2002/364 — **verified**.
  - HR 22 januari 1999, ECLI:NL:HR:1999:ZC2831 (Uneto) — **medium confidence**.
- **Interaction with:** A5, A6, E2.
- **Consequence:** Bepaalt per norm welk rechtsgevolg intreedt; motiveringseis voor rechter.

---

### E2. Art. 3:40 BW en EU-dwingend recht
**RAG_TAG:** `nl.bw.3_40.eu_mandatory_interaction`

- **Doctrine:** EU-dwingend recht (mededingingsrecht, financiële regulatie, consumentenbescherming) grijpt via art. 3:40 BW in op nationale contractuele geldigheid.
- **Function:** Validity gate voor EU-dwingendrechtelijke normen.
- **Toets:**
  - **Kartelverbod (art. 101 TFEU / art. 6 Mw):** art. 101(2) TFEU verklaart strijdige afspraken **nietig van rechtswege**; ambtshalve toepasselijk (Eco Swiss C-126/97); gevolgt Nederlandse 3:40 lid 2 BW-vertaling.
  - **Wft / financiële regulatie:** overtreding van gedrags- of prudentiële normen leidt **niet zonder meer** tot nietigheid; strekking-toets; veelal alleen civielrechtelijke zorgplichtvordering/schadevergoeding.
  - **Consumentendwingend recht:** zie B5.
- **Leading cases:**
  - **CJEU Eco Swiss C-126/97** — **verified**. Art. 101 TFEU als openbare orde; ambtshalve toetsing bij vernietiging arbitraal vonnis.
  - **CJEU Courage/Crehan C-453/99** — **verified**. Ook partij bij kartel kan schadevergoeding vorderen; nietigheid verhindert dit niet.
  - **CJEU Manfredi C-295/04–298/04** — **verified**. Vervolgrechtspraak.
  - **HR 5 april 2013, ECLI:NL:HR:2013:BY8101 (Lundiform/Mexx)** — **verified generally**; Haviltex + exoneratie + commercial context, zijdelings relevant.
  - HR-rechtspraak over Wft-zorgplicht: HR 5 juni 2009, ECLI:NL:HR:2009:BH2815 (De Treek/Dexia), NJ 2012/182 — **verified**; effectenlease zorgplicht; geen automatische nietigheid.
- **Interaction with:** A5, A6, E1, B5.
- **Consequence:** Vaak vernietigbaarheid/schadevergoeding, zelden automatische nietigheid buiten art. 101(2) TFEU.

---

### E3. Partiële nietigheid — art. 3:41 BW
**RAG_TAG:** `nl.bw.3_41.partiele_nietigheid`

- **Doctrine:** Als een grond van nietigheid/vernietigbaarheid slechts een deel van een rechtshandeling betreft, blijft de rest in stand voor zover dit, gelet op inhoud en strekking, niet in onverbrekelijk verband staat met het aangetaste deel.
- **Function:** Severability-toets.
- **Toets:**
  1. Is de nietigheidsgrond bedingsbegrensd (bv. één clause oneerlijk)?
  2. Staat de rest in "onverbrekelijk verband"? (inhoud, strekking, totstandkoming, partijwil)
  3. Zou een redelijke partij de rest ook zijn aangegaan?
  - Voor consumenten: CJEU Banco Español — rechter mag oneerlijk beding niet matigen; alleen buiten toepassing laten, tenzij overeenkomst daardoor onuitvoerbaar wordt en dit de consument benadeelt (Kásler).
- **Leading cases:**
  - CJEU Banco Español de Crédito C-618/10 — **verified**.
  - CJEU Kásler C-26/13 — **verified**.
  - HR 20 december 2013, ECLI:NL:HR:2013:2123 — **medium confidence**; partiële nietigheid in commerciële context.
  - HR 14 juni 2002, ECLI:NL:HR:2002:AE0659 (Bramer/Colpro) — **medium confidence**; onverbrekelijk verband test.
- **Interaction with:** Alle nietigheids-/vernietigbaarheidsgronden.
- **Consequence:** Overeenkomst blijft "gezond" deel geldig, of valt in zijn geheel weg.

---

### E4. Conversie — art. 3:42 BW
**RAG_TAG:** `nl.bw.3_42.conversie`

- **Doctrine:** Nietige rechtshandeling kan worden geconverteerd in een wel geldige, indien (a) de geldige handeling in betekenis zodanig met de nietige overeenkomt dat aangenomen mag worden dat zij zou zijn verricht als de ongeldigheid bekend was geweest, en (b) dit niet onredelijk zou zijn jegens een partij die zich tegen conversie verzet.
- **Function:** Validity rescue; past op nietigheid, niet op vernietigbaarheid.
- **Toets:**
  1. Nietige rechtshandeling aanwezig.
  2. Alternatieve rechtshandeling die geldig is en in betekenis zodanig overeenkomt.
  3. Hypothetische partijwil: zouden partijen dit bij bekendheid met de nietigheid zijn aangegaan?
  4. Redelijkheidstoets jegens bezwarende partij.
- **Leading cases:**
  - **HR 21 januari 1944, NJ 1944/120 (van der Water/Van Hemme)** — klassiek — onder oud BW, maar doctrinaal nog relevant.
  - HR 22 november 2002, ECLI:NL:HR:2002:AE8185, NJ 2003/34 — **verified**. Ambtshalve toepassing conversie binnen grenzen rechtsstrijd (iura novit curia, art. 25 Rv).
- **Interaction with:** A3, A4, A5, A6.
- **Consequence:** Nietige handeling wordt vervangen door een geldige met zoveel mogelijk dezelfde rechtsgevolgen.

---

### E5. Bekrachtiging — arts. 3:55 & 3:58 BW
**RAG_TAG:** `nl.bw.3_55_58.bekrachtiging`

- **Doctrine:**
  - Art. 3:55 BW: **vernietigbare** rechtshandelingen kunnen worden bekrachtigd door de bevoegde partij; de bevoegdheid tot vernietiging vervalt daarmee.
  - Art. 3:58 BW: gebreken in de wijze van totstandkoming worden geheeld indien alle onmiddellijk belanghebbenden de handeling als geldig hebben aanvaard ("bekrachtiging met terugwerkende kracht").
  - Art. 3:69 BW: bekrachtiging van onbevoegd verrichte handeling door de vertegenwoordigde.
- **Function:** Waiver of annulability; heling van vormfouten.
- **Toets:** (a) wie bekrachtigt, is daartoe bevoegd; (b) handeling door alle onmiddellijk belanghebbenden aanvaard (3:58); (c) geen rechten van derden aangetast; (d) geen nietigheid van rechtswege (niet bekrachtigbaar).
- **Leading cases:** Rechtspraak relatief casuïstisch; geen dominant modern HR-arrest dat doctrinaal stuurt. Flag: "no clear leading HR case — use Asser/Hartkamp 3-I."
- **Interaction with:** A1, A2, A7, A8, A9, A10, A11, A12.
- **Consequence:** Vernietigingsbevoegdheid vervalt; rechtshandeling blijft onaantastbaar.

---

### E6. Absolute vs. relatieve nietigheid & ambtshalve toepassing
**RAG_TAG:** `nl.bw.nietigheid_absolute_vs_relatief`

- **Doctrine:** Nederlands recht kent formeel twee sancties — **nietig** (van rechtswege) en **vernietigbaar** (op inroep). Binnen "nietigheid" is procedureel relevant het onderscheid tussen **absolute** (werkt jegens iedereen, ambtshalve toepasselijk, door eenieder inroepbaar) en **relatieve** nietigheid (bv. pauliana 3:45 BW — alleen jegens inroepende schuldeiser).
- **Function:** Regelt wie mag inroepen, ambtshalve-plicht, derdenwerking.
- **Toets (samengevat):**
  - **Absolute nietigheid** (3:40 lid 1; 3:39 vormgebrek constitutief; 101(2) TFEU): eenieder; rechter ambtshalve; erga omnes.
  - **Protectieve nietigheid** (3:40 lid 2 tweede limb; 6:233 jo. 6:236/237): slechts beschermde partij; rechter ambtshalve bij consument + Richtlijn 93/13; verjaring via 3:52.
  - **Relatieve nietigheid** (3:45 BW pauliana): alleen inroepende schuldeiser; werkt alleen jegens hem.
  - **Vernietigbaar** (3:44; 6:228; 1:89; 2:7): alleen bevoegde; 3:52 BW verjaring; ambtshalve in principe niet, tenzij openbare orde (zie ambtshalve-rechtspraak).
- **Leading cases:** Zie E1, E2, B5 voor ambtshalve-toepassing lijn. Procedurele kern: HR 13 september 2013, ECLI:NL:HR:2013:691 (Heesakkers/Voets) — **verified**; openbare-orde-kwalificatie Richtlijn 93/13 normen. HR 22 november 2002, ECLI:NL:HR:2002:AE8185 — **verified**; ambtshalve toepassing conversie. HR 20 januari 2006, ECLI:NL:HR:2006:AU4122, NJ 2006/80 — **verified**; art. 6:89 BW **niet** ambtshalve.
- **Interaction with:** Alle Part A–D-gronden.
- **Consequence:** Bepaalt procedurele verwerking in de RAG-pipeline: wie kan chunk invoken, of de rechter het verplicht is, en derdenwerking.

---

## Verification summary & known gaps

Strongly verified (directly fetched or consistently cited across rechtspraak.nl, cassatieblog.nl, NJ, and university sources): Esmilo/Mediq, Parkeerexploitatie/Amsterdam, OZF/AZL, Baris/Riezenkamp, Van Geest/Nederlof, Van Elmbt/Feierabend, S'Energy/Delta, Kribbebijter, ING/Bera, HR 3 februari 2017 (risicoleer), HR 14 oktober 2022 (Zilveren Kruis/IPGGZ), Heesakkers/Voets, HR 26 februari 2016 (boetebeding huur), HR 29 april 2016 (SEBA/Amsterdam), HR 21 april 2017 (Dexia), HR 22 november 2019 (ABN AMRO hypotheek), HR 24 november 2023 (verzettermijn), Banco Español C-618/10, Pannon C-243/08, Mostaza Claro C-168/05, Asturcom C-40/08, Eco Swiss C-126/97, Courage/Crehan C-453/99, Unamar C-184/12, Nikiforidis C-135/15, El Majdoub C-322/14, Briljant Schreuders/ABP, Campina/Van Jole, VvdE/CSM, Pouw/Visser, Ploum/Smeets II, Van de Steeg/Rabobank, Tan/Forward, Brocacef/Simons, Saelman, Van Hese/De Schelde, Van Dooren q.q./ABN AMRO I-II-III, Ontvanger/Pelicaan, Geurtzen/Kampstaal, First Data/KPN.

Medium confidence (should be re-verified at pinpoint level before deployment): Van Geest/Nederlof ECLI:NL:HR:1990:ZC0088 (citation confirmed; pinpoint may differ), HR 11 december 2009 (art. 3:34), HR 11 juli 2008 (wilsvertrouwensleer), HR 9 december 2011 (art. 7:2), HR 22 januari 1999 (Uneto), HR 13 juli 2007 (1:88), HR 29 november 2002 (1:88), HR 14 juni 2002 (Bramer/Colpro), HR 4 mei 2018 (stuiting), HR 11 september 2020 (verval), HR 2 februari 2018 (bepaalbaarheid), HR 17 juni 2005 (bepaalbaarheid), HR 18 september 2020 (forumkeuze), HR 31 oktober 2014 (beslagvrije voet), HR 20 december 2013 (partiële nietigheid), HR 5 april 2013 (Lundiform/Mexx — verified case, relevance to E2 is doctrinal rather than direct).

Flagged as having no single dominant modern HR case: bedrog (A8), bedreiging (A9), bekrachtiging (E5), beslagverboden (D6). For these, the statutory text and Asser/Hartkamp–Sieburgh commentary are the primary authorities; the taxonomy chunks explicitly state this.

Do not treat any "LOW CONFIDENCE" or "medium confidence" tag as authoritative without the RAG system re-verifying against rechtspraak.nl or a primary NJ/JOR source. The chunking schema (`RAG_TAG`) is stable and may be used as the metadata key for retrieval; each chunk is self-contained with the nine required fields plus cross-references.