# SEO & AI Optimization Research – meteleska.com

**Audited URL:** https://www.meteleska.com/cs/ (and related pages)
**Date of audit:** 26 May 2026
**Scope:** Live website only (rendered content, public URLs, search visibility). No source-code review.

---

## 1. Executive summary

The website is a brand-presence site for the band Meteleska. Visually it does its job, but from an SEO / "AI Search" (LLM, Google AI Overviews, Perplexity, Bing Copilot…) perspective it is significantly underperforming. Crawlers and language models cannot reliably extract:

- who the band is,
- what they sound like,
- when and where they play,
- where to listen / book them.

The biggest red flags found during the audit:

1. **`robots.txt` returns 404** – https://www.meteleska.com/robots.txt
2. **`sitemap.xml` returns 404** – https://www.meteleska.com/sitemap.xml
3. **`site:meteleska.com` in Google returns no usable results** – the domain is effectively invisible in indexed search; users searching "Meteleska" are pushed toward third-party sources (Bandzone, SoundCloud) or the unrelated "MeteleskuBlesku" site.
4. **Empty / near-empty pages** – `News`, `Music` and `Gallery` render only a heading; there is no crawlable text or structured data for an AI to summarise.
5. **URL inconsistency / broken menu links** – the menu links to `https://www.meteleska.com/concerts` (no language prefix), while `https://www.meteleska.com/cs/shows/` returns **404**. Mixed `/cs/` vs unprefixed routes confuse crawlers and break hreflang.
6. **Concerts page is purely historical** – latest entry is 20. 9. 2025; there is no "upcoming shows" section. Both Google search and AI summarisers therefore conclude "no planned concerts" – which is the literal answer they will give users.
7. **No structured data (Schema.org)** for `MusicGroup`, `MusicEvent`, `MusicAlbum` or `Person`. This is exactly the data Google and LLMs use to build artist knowledge panels and event answers.
8. **Bio is extremely short** (~150 words CZ, ~40 words EN) and contains a typo ("Energeticko-energickým", "Pthoto by"). Insufficient for any meaningful AI snippet.
9. **Czech-only footer ("Děkujeme…") on the English page** – signals to Google that the EN page is not fully localised.
10. **Social icons have empty anchor text** (`[**](https://...)`), giving search engines no link context and failing accessibility.

A few hours of content/markup work could move this site from "invisible" to "default first result for the band name in CZ + appearing in AI Overviews".

---

## 2. What the site looks like to a crawler / AI today

This is the entire crawlable text of the Czech homepage as seen by a non-JS user agent:

```
Meteleska
MENU
Meteleska
Hudba
News
Fotogalerie
Bio
Kapela Meteleska hraje především hudbu co diváky roztančí. Mezi žánry je
těžko zařaditelná – hudba je směsí rocku, reggae, ska, punku, folklóru i
balkánu. … Meteleska je kapela, kterou stojí zato prožít na živo.
Booking
+420 775 367 426 info@meteleska.com
Ke stažení
Press fotografie ve vysokém rozlišení (38,2 MB)
Děkujeme všemu co nás podporuje! Thanks to all that support us!
```

That is everything an LLM has to work with. There is:

- no `<title>`/`<meta description>` visible in the rendered content layer,
- no Open Graph preview content beyond what is implicit,
- no list of band members,
- no discography,
- no genre tags,
- no list of upcoming shows,
- no embedded audio / video,
- no Schema.org markup.

The English homepage is even thinner (~5 sentences) and ends with a Czech-language footer, which weakens it as a separate locale.

---

## 3. Findings & recommendations

Items are ordered by impact ÷ effort. Tackle them top-to-bottom.

### 3.1 Critical – do these first

#### F-1. Publish `robots.txt`

Currently 404. Add the file at `https://www.meteleska.com/robots.txt`:

```
User-agent: *
Allow: /

# AI crawlers (explicitly allow if you want to appear in AI answers)
User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://www.meteleska.com/sitemap.xml
```

If you ever decide you don't want to feed LLMs, change `Allow: /` to `Disallow: /` for those user agents. The point is to make a conscious choice; today the absence of robots.txt is interpreted as "anything goes" but also signals that the site is unmaintained.

#### F-2. Publish `sitemap.xml`

Generate an XML sitemap that lists every public URL in both languages, with `<xhtml:link rel="alternate" hreflang="…">` annotations. Minimal example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://www.meteleska.com/cs/</loc>
    <xhtml:link rel="alternate" hreflang="cs" href="https://www.meteleska.com/cs/"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://www.meteleska.com/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.meteleska.com/cs/"/>
    <lastmod>2026-05-26</lastmod>
  </url>
  <!-- repeat for bio, music, shows, gallery, news, contact -->
</urlset>
```

Then submit it in **Google Search Console** and **Seznam Webmaster** (Czech search engine – Meteleska's primary audience).

#### F-3. Fix URL & menu consistency

The current state:

| Menu link | What you'd expect | What it actually does |
|---|---|---|
| `Shows` → `/concerts` | `/cs/concerts/` or `/cs/shows/` | Resolves, but unprefixed → loses locale context |
| `/cs/shows/` | Shows in Czech | **404** |
| `/cs/music/` | Music in Czech | Empty page |
| `/cs/news/` | News in Czech | Empty page |

Pick **one** convention (recommended: `/cs/shows/`, `/en/shows/`) and 301-redirect everything else to it. Make sure menu links honour the user's current locale. Mixed prefixed/unprefixed URLs cause Google to index duplicate content and prevent hreflang from working.

#### F-4. Add a real "Upcoming shows" section

Today the only thing both search and AI can say about Meteleska's concerts is "the most recent entry is 20. 9. 2025; no upcoming shows are listed." This is exactly the AI answer your Czech fans got when I tested.

Action items:

- Split the shows page into **"Připravované koncerty / Upcoming"** and **"Proběhlé koncerty / Past"**.
- Always show at least the next 1–3 events on the homepage, even if it is a single line "Next gig: TBA – sign up for the newsletter".
- Mark every event up with `MusicEvent` Schema.org (see F-6).

#### F-5. Write proper `<title>` and `<meta name="description">` for every page

Suggested values (Czech / English):

| Page | `<title>` | `<meta name="description">` |
|---|---|---|
| `/cs/` | `Meteleska – česká kapela, rock, reggae, ska, balkán | Praha` | `Meteleska je pražská kapela hrající energickou směs rocku, reggae, ska, punku a balkánu. Koncerty, hudba, booking.` |
| `/en/` | `Meteleska – Czech reggae / ska / world music band from Prague` | `Meteleska is a Prague-based band blending reggae, ska, rock, gypsy and world music. Live shows, music, booking.` |
| `/cs/bio/` | `Bio kapely Meteleska – členové, žánr, historie od 2008` | `Kapela Meteleska vznikla v prosinci 2008 v Praze-Kbelech. Přečtěte si o členech, stylu a historii kapely.` |
| `/cs/music/` | `Hudba – Meteleska na Spotify, YouTube, Bandzone` | `Poslechněte si nahrávky Metelesky – Jah Je, Jsi Mistr, Sedm mužů a další skladby na Spotify, YouTube a Bandzone.` |
| `/cs/news/` | `Novinky – Meteleska` | `Aktuální zprávy o kapele Meteleska – nové klipy, koncerty a další aktivity.` |
| `/cs/gallery/` | `Fotogalerie – Meteleska live & promo` | `Fotografie z koncertů Metelesky (Palác Akropolis, Cross Club, festivaly) a promo fotografie.` |
| `/cs/contact/` | `Booking – Meteleska | info@meteleska.com, +420 775 367 426` | `Booking, rider a press materiály kapely Meteleska. Kontaktujte nás pro zajištění koncertu.` |

Keep `<title>` under ~60 characters and meta description ~150–160.

### 3.2 High impact – structured data for AI

#### F-6. Schema.org JSON-LD on every page

This is the single highest-leverage change for AI visibility. Add the following to the `<head>` of `/cs/` and `/en/` (and a per-event copy on the shows page):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MusicGroup",
  "name": "Meteleska",
  "url": "https://www.meteleska.com/",
  "logo": "https://www.meteleska.com/static/assets/img/logo.png",
  "image": "https://www.meteleska.com/static/assets/img/press-photo.jpg",
  "foundingDate": "2008-12",
  "foundingLocation": {
    "@type": "Place",
    "name": "Praha-Kbely, Česká republika"
  },
  "genre": ["Reggae", "Ska", "Rock", "World music", "Balkan", "Punk"],
  "email": "info@meteleska.com",
  "telephone": "+420775367426",
  "sameAs": [
    "https://open.spotify.com/artist/2KXCfv6kpS710QG3dB0ILF",
    "https://facebook.com/meteleska",
    "https://instagram.com/meteleska",
    "https://youtube.com/user/meteleska",
    "https://bandzone.cz/meteleska",
    "https://twitter.com/meteleska",
    "https://soundcloud.com/meteleska"
  ],
  "member": [
    { "@type": "Person", "name": "…", "roleName": "Housle, hlavní vokál" },
    { "@type": "Person", "name": "…", "roleName": "Baskytara" }
  ]
}
</script>
```

For every concert on the shows page:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MusicEvent",
  "name": "Meteleska – Cosmir Fest",
  "startDate": "2025-09-20T20:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "Sokolovna Měšice",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Měšice",
      "addressCountry": "CZ"
    }
  },
  "performer": { "@type": "MusicGroup", "name": "Meteleska" },
  "offers": {
    "@type": "Offer",
    "url": "https://…ticket-url…",
    "availability": "https://schema.org/InStock"
  }
}
</script>
```

This single change is what makes Google show a knowledge panel for the band, and it's what makes Perplexity / ChatGPT / Google AI Overviews answer "Meteleska is a Czech reggae/ska band from Prague founded in 2008" instead of confusing them with the unrelated *MeteleskuBlesku* site.

Validate with https://search.google.com/test/rich-results.

#### F-7. Open Graph & Twitter Card meta tags

For nice link previews on Facebook, Messenger, Twitter/X, Discord, Slack, etc.:

```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="Meteleska">
<meta property="og:title" content="Meteleska – česká kapela, rock / reggae / ska / balkán">
<meta property="og:description" content="Pražská kapela hrající energickou směs rocku, reggae, ska, punku a balkánu.">
<meta property="og:image" content="https://www.meteleska.com/static/assets/img/og-cover-1200x630.jpg">
<meta property="og:url" content="https://www.meteleska.com/cs/">
<meta property="og:locale" content="cs_CZ">
<meta property="og:locale:alternate" content="en_US">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@meteleska">
```

Make sure `og:image` is a real 1200×630 JPG/PNG that exists.

#### F-8. Proper hreflang & `<link rel="canonical">`

In the `<head>` of every page:

```html
<link rel="canonical" href="https://www.meteleska.com/cs/bio/">
<link rel="alternate" hreflang="cs" href="https://www.meteleska.com/cs/bio/">
<link rel="alternate" hreflang="en" href="https://www.meteleska.com/en/bio/">
<link rel="alternate" hreflang="x-default" href="https://www.meteleska.com/cs/bio/">
```

Set the document language correctly: `<html lang="cs">` on Czech pages, `<html lang="en">` on English pages.

### 3.3 Medium impact – fill the empty pages

LLMs cannot summarise what isn't there. Right now these pages are essentially blank.

#### F-9. `/cs/music/` and `/en/music/`

Currently shows only the heading. Add:

- Embedded **Spotify** player (already linked) – the official `<iframe>` widget.
- Embedded **YouTube** player(s) for the most important videos.
- A simple plain-text **discography**: list each track / single / EP with year and a short description. AI will not transcribe the iframe – it needs text.
- Recommended structure per release:

```html
<article>
  <h2>Jah Je (2012)</h2>
  <p>Singl Metelesky vydaný v roce 2012, mix reggae a ska. Pokřtěn 20. 1. 2012 v KC Kaštan v Praze.</p>
  <p><a href="https://open.spotify.com/...">Poslechnout na Spotify</a> · <a href="https://youtu.be/...">YouTube</a></p>
</article>
```

#### F-10. `/cs/news/` and `/en/news/`

Today the page exists but has no listed news items. Either:

- Publish a few short posts (klip, koncert, novinka v sestavě, …) so the page has crawlable content, **or**
- Hide the page from the menu and `noindex` it until you have content – an indexed empty page hurts rankings.

The bare minimum: re-purpose the page as an "Aktuality" feed that pulls automatically from the band's Facebook or Instagram if manual posting is too much work.

#### F-11. `/cs/gallery/` – add alt text and per-photo metadata

The page lists galleries by section ("Klubovna 2020", "Palác Akropolis", …) but every image is presented without text context. For each image:

- Meaningful `alt="…"` attribute (description of what is in the photo, where, when).
- Filename should be descriptive (`meteleska-akropolis-2018-koncert.jpg`, not `IMG_4561.jpg`).
- Lazy-loading (`loading="lazy"`) for everything below the fold.
- Use modern formats (`<picture>` with WebP / AVIF) – this also boosts Core Web Vitals.

#### F-12. Expand the Bio

The CZ bio is ~150 words; the EN bio is ~40 words. Aim for 300–500 words of original copy that includes:

- founding year, place, founding members,
- a sentence or two per current member (name, instrument, fun fact),
- genres they play and their influences,
- notable shows / festivals / collaborations,
- a discography summary with release dates,
- press quotes if any.

Also fix existing copy issues:

- "Energeticko-energickým" – probable typo, intended "Energetickým" or "Energeticko-rytmickým".
- "Pthoto by" on the gallery page → "Photo by".

#### F-13. Localise the footer

The English homepage currently ends with the Czech sentence "Děkujeme všemu co nás podporuje! Thanks to all that support us!" – the first half should be removed (or replaced with "Thanks to everyone who supports us!") on `/en/` so Google sees a fully English page.

### 3.4 Lower priority but worth doing

#### F-14. Replace empty-anchor social icons with named links

Today, social icons appear in HTML as `[**](https://facebook.com/meteleska)` – the visible text is `**` (or a font-icon glyph). Use a real `aria-label` and visually-hidden text:

```html
<a href="https://facebook.com/meteleska" aria-label="Meteleska na Facebooku" rel="me noopener">
  <svg aria-hidden="true">…</svg>
  <span class="sr-only">Facebook</span>
</a>
```

Same for Spotify, Instagram, YouTube, Bandzone, Twitter/X, SoundCloud. This:

- gives Google link context (anchor text matters),
- makes the social profiles count as `sameAs` for Schema.org,
- fixes accessibility / WCAG 2.1 4.1.2.

#### F-15. Heading hierarchy

The homepage currently renders three `<h2>` headings ("Hudba", "News", "Fotogalerie", "Bio") that link to other pages but have no body text under them. Either:

- Put 1–2 sentences of intro text under each heading (preferred), or
- Convert them from `<h2>` to plain styled links so the heading outline isn't misleading.

#### F-16. Performance & Core Web Vitals

Run a Lighthouse / PageSpeed Insights audit (https://pagespeed.web.dev/?url=https%3A%2F%2Fwww.meteleska.com%2Fcs%2F) and target:

- **LCP** < 2.5 s — the press / hero image should be `width`/`height` attributed, preloaded, and served as WebP.
- **CLS** < 0.1 — reserve space for the menu, hero, and gallery thumbnails.
- **INP** < 200 ms.

Concrete actions:

- Compress press JPGs (the 38.2 MB ZIP suggests originals are huge; the on-page images may be unoptimised too).
- Add `loading="lazy"` and `decoding="async"` to images below the fold.
- Serve static assets with long `Cache-Control` (1 year + content hash in filename).
- Enable HTTP/2 or HTTP/3 and Brotli compression on the server.

#### F-17. HTTPS / redirect hygiene

- Confirm `http://` → `https://` 301 redirect.
- Confirm `meteleska.com` → `www.meteleska.com` (or the other way) is a single 301 hop. Don't chain redirects.
- Confirm trailing-slash normalisation (today menu links mix `/cs/news/` with `/concerts` – pick one).

#### F-18. Sign the site up in places search engines and AI scrape

- **Google Search Console** – submit sitemap, monitor coverage and Core Web Vitals.
- **Seznam Webmaster** (https://www.seznam.cz/) – essential for the Czech audience.
- **Bing Webmaster Tools** – Bing's index also powers ChatGPT, Copilot and DuckDuckGo.
- **Wikipedia / Wikidata** – create or update a Wikidata entry (`instance of: music group`) with band members, formation year, official website, genres, social links. Wikidata is one of the primary structured sources LLMs train on.
- **MusicBrainz** – create / claim the artist entry; this is the canonical music-metadata source used by Spotify, Apple Music, Wikipedia, and many LLMs.
- **Google Business Profile** – optional but useful: lets Czech users find booking info directly from Google Maps / Search.

#### F-19. Internal linking

Today the menu repeats on every page but there are virtually no in-body links. Add contextual links inside the Bio (e.g. "od svého prvního koncertu v Baru Zahrada" → link to that show on `/cs/shows/`, "vydali jsme klip Jah Je v roce 2012" → link to `/cs/music/#jah-je`). This helps both crawlers discover deep pages and AI build richer summaries.

#### F-20. Keep an evergreen "AI-friendly" paragraph on the homepage

LLMs love a single clean paragraph that answers "who, what, where, when, genres, links". Add a hidden-from-design-but-visible-to-text paragraph near the top of `/cs/` and `/en/`, something like:

> Meteleska je česká kapela založená v prosinci 2008 v Praze (Kbely). Hraje směs reggae, ska, rocku, balkánu, folklóru a punku. Sestavu tvoří … (jména členů). Vydala mj. singly „Jah Je" (2012) a „Jsi Mistr" (2012). Pravidelně koncertuje v Praze (Cross Club, Palác Akropolis, KC Kaštan) i na festivalech. Booking: info@meteleska.com, +420 775 367 426.

Concrete, factual, link-rich – exactly the format AI Overviews and Perplexity quote verbatim.

---

## 4. Suggested rollout order

1. **Week 1 – low-effort, high impact:** F-1 robots.txt, F-2 sitemap.xml, F-3 URL consistency, F-5 titles & descriptions, F-7 OG tags, F-8 hreflang/canonical, F-13 footer localisation, F-14 social link a11y.
2. **Week 2 – schema & content:** F-6 JSON-LD MusicGroup + MusicEvent, F-4 Upcoming shows, F-12 expanded bio, F-15 headings.
3. **Week 3 – fill empty pages:** F-9 Music with embeds & text, F-10 News strategy, F-11 Gallery alt text.
4. **Week 4 – performance & external presence:** F-16 Core Web Vitals, F-17 redirect hygiene, F-18 Search Console / Seznam / Wikidata / MusicBrainz, F-19 internal links, F-20 AI-friendly paragraph.

After rollout, re-test with:

- https://search.google.com/test/rich-results (per page),
- https://search.google.com/search-console (coverage report),
- https://pagespeed.web.dev/,
- a manual query `site:meteleska.com` – which today returns **nothing useful**; the goal is that within ~2 weeks of submission it returns the full set of indexed pages.

---

## 5. Quick wins checklist (copy/paste into an issue tracker)

- [ ] Publish `/robots.txt` with `Sitemap:` line.
- [ ] Publish `/sitemap.xml` with all CZ + EN URLs + hreflang annotations.
- [ ] Submit sitemap to Google Search Console and Seznam Webmaster.
- [ ] Unify URLs: kill `/concerts`, use `/cs/shows/` and `/en/shows/`, 301 the rest.
- [ ] Fix 404 on `/cs/shows/` and `/en/shows/`.
- [ ] Add unique `<title>` and `<meta description>` to every page.
- [ ] Add `<link rel="canonical">` and full hreflang set to every page.
- [ ] Set `<html lang="cs">` / `<html lang="en">` correctly.
- [ ] Add `MusicGroup` JSON-LD on `/cs/` and `/en/`.
- [ ] Add `MusicEvent` JSON-LD per concert on the shows page.
- [ ] Add Open Graph + Twitter Card meta tags + a 1200×630 cover image.
- [ ] Split shows into "Upcoming" and "Past"; always show at least 1 upcoming entry (or "TBA").
- [ ] Expand bio to 300–500 words in CZ + EN; list members and instruments.
- [ ] Fix typos: "Energeticko-energickým", "Pthoto by".
- [ ] Translate the Czech "Děkujeme…" footer on the English version.
- [ ] Add a Spotify and YouTube embed + textual discography on `/cs/music/`.
- [ ] Either publish news posts or `noindex` the empty `/cs/news/` page.
- [ ] Give every image a descriptive `alt`, descriptive filename, `loading="lazy"`.
- [ ] Replace empty-text `**` social links with real `aria-label`s.
- [ ] Compress hero/press images, target LCP < 2.5 s.
- [ ] Create / update Wikidata + MusicBrainz entries.
- [ ] Add a single factual "AI-friendly" intro paragraph (who/what/where/when/booking).

---

## 6. Notes on AI-search specifically (LLMs, AI Overviews, Perplexity, Copilot)

Beyond classic SEO, the things that disproportionately help LLMs are:

- **Schema.org JSON-LD** (F-6) – LLMs read it directly during training and at retrieval time.
- **Plain prose facts** in the body (F-12, F-20) – LLMs cannot parse iframes, audio, or images, so a single textual paragraph stating the facts of the band is gold.
- **Cross-source consistency** – the band name, founding year, members, and genres should match across `meteleska.com`, Wikidata, MusicBrainz, Bandzone, Spotify, Facebook. LLMs weight facts that appear in multiple independent sources; inconsistency causes them to refuse or hedge.
- **Explicit opt-in for AI crawlers** in `robots.txt` (F-1). Without it, several AI crawlers will skip the site by default (Google-Extended in particular).
- **Avoid namespace collisions** – "Meteleska" vs the popular "MeteleskuBlesku" site is a real disambiguation problem for LLMs. A strong Wikidata entry and explicit Schema.org `MusicGroup` are the cleanest way to separate the two entities in the AI's mind.

If only one thing on this list gets implemented, it should be **F-6 (Schema.org JSON-LD for the band and the events)** combined with **F-1+F-2 (robots.txt + sitemap.xml)**. Those three changes alone will dramatically improve both classic SEO and AI search visibility.
