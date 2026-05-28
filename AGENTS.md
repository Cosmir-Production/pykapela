# AGENTS.md

Quick orientation for AI coding agents. Read this first; it will save you a full repo scan.

## What this project is

`pykapela` is a **Django website template for music bands** (the word means
"about a band" in Czech). The same codebase is deployed on **multiple band
websites** (e.g. meteleska.com, sfmagdalena, …). Each deployment shares the
code but holds its own database, media, translations and theme overrides.

The audited site that ships with this checkout is **Meteleska**, but **never
hard-code any band-specific content, branding, social URLs, contact info,
genres, member names, dates, etc.** All of that lives in the database. See
"Where the content lives" below.

> If you're tempted to put a band name, phone number, social link, genre,
> color, logo path, page title, footer slogan, etc. into a `.py` / `.html` /
> `.scss` file, **stop**. It almost certainly belongs in a DB model (usually
> `Preference`, `Page`, `Social`, `Event`, `MenuItem` or a `photologue.Gallery`).

## Stack & runtime

- **Python 3.7.6** (`runtime.txt`), **Django 3.1.1**, PostgreSQL via `psycopg2`.
- Deployed Heroku-style: `Procfile` → `gunicorn pykapela.wsgi --preload`,
  release phase runs `./release.sh` (makemigrations + migrate).
- WSGI entry: `pykapela/wsgi.py` → `DJANGO_SETTINGS_MODULE=pykapela.settings`.
- `pykapela/settings/__init__.py` composes the real settings from split
  modules: `main`, `app`, `tinymce`, `database`, `storage`, `settings_local`,
  `translation_manager`, `logging`, `emails`. The last imports win, so
  `settings_local.py` (gitignored) overrides everything for that deployment.
- `database.py` and `settings_local.py` are **per-deployment & gitignored**.
  `*.default.py` versions exist as templates.
- Frontend toolchain: **Foundation 6 + Gulp + SCSS** (`gulpfile.babel.js`),
  Node deps in `package.json` / `yarn.lock`.

## Key third-party Django apps (don't reinvent)

| Concern | Package | Used for |
|---|---|---|
| Menu / sitetree | `django-sitetree` | Main menu items, per-locale, override models in `pykapela.menu` (`MenuTree`, `MenuItem`). Seeded from `treedump.json` via `sitetreeload`. |
| i18n on DB fields | `django-modeltranslation` | Per-language fields on `Page` (title, content) and `MenuItem` (title). Configured in `<app>/translation.py`. |
| Translation workflow | `django-translation-manager` | Admin UI to edit `.po` strings. See `Working with Translation Manager` in `README.md`. |
| Gallery / photos | `django-photologue` (+ `pykapela.photologue_custom`) | Galleries, photos, thumbnails. We extend `Gallery` with `GalleryExtended` (tags via `django-taggit`) and a `PykapelaGallery` proxy. |
| WYSIWYG | `django-tinymce` | `HTMLField` on `Page.content`, `Event.description`. |
| Storage | `django-storages` | S3 backend wired in `settings/storage.py` (currently commented out, opt-in per deployment). |
| Redirects | `django.contrib.redirects` | Old → new URL mappings from the admin. |

When adding behaviour, prefer extending these libraries through their
documented hooks (e.g. `TranslationOptions`, `TreeItemBase`) instead of
forking templates or models.

## Project layout

```
manage.py                   # standard Django entry
release.sh                  # heroku release-phase hook
Procfile                    # gunicorn + release
requirements.txt            # pinned Python deps
runtime.txt                 # python-3.7.6
package.json / gulpfile     # frontend build
treedump.json               # sitetree main_menu seed

pykapela/
  settings/                 # split settings (see above)
  urls.py                   # root urlconf, i18n_patterns under /<lang>/
  views.py                  # WebView -> homepage (index.html)
  wsgi.py

  base/                     # BaseView, BaseModel (created/changed timestamps),
                            # context preparation (`_prepare_context`),
                            # `tt_urls` templatetag (language switch helper).
  preferences/              # Preference singleton (pk=1) – site-wide config
  pages/                    # CMS pages (slug-based, HTML content from TinyMCE)
  events/                   # concerts: Event model, /concerts/ + /<slug>/
  gallery/                  # views wrapping photologue + PykapelaGallery
  photologue_custom/        # extensions on top of photologue's Gallery
  menu/                     # MenuTree / MenuItem (sitetree overrides)
  social/                   # Social links + embed widgets (FB / Twitter / …)
  files/                    # generic admin file uploads
  app/                      # custom mgmt commands + static-asset destination
    management/commands/    # seed_database, grab_social_content
    static/                 # gulp build output (collected by collectstatic)
  src/assets/               # SCSS + JS sources (input to gulp)
    scss/themes/            # per-site theme stubs (e.g. meteleska.scss)
  templates/                # base.html, index.html, page.html, events/, …
  locale/                   # .po files for CZ/EN UI strings
```

Note the **two `static/` directories**:
- `pykapela/app/static/` – **gulp build output** (compiled CSS/JS/img).
- `pykapela/static/` – legacy/gitignored, populated by `collectstatic` at deploy.

## Where the content lives (DB-driven, not codebase-driven)

Every piece of human-facing content must come from one of these models so the
codebase stays band-agnostic.

| Model | Source file | What it stores |
|---|---|---|
| `preferences.Preference` (singleton, pk=1) | `pykapela/preferences/models.py` | `site_name`, `slogan`, `title_slogan`, `description`, `footer_slogan`, `footer_copyright`, `email`, `phone`, `primary_color`, `secondary_color`, `custom_css`, `logo`, `favicon`, `rider_file`, `press_zip_file`, `logo_file`, `google_analytics`, `promoted_gallery` (gallery id for homepage), `show_languages`. Each field is exposed in templates as `{{ config_<field_name> }}` via `Preference.get_values()`. |
| `pages.Page` | `pykapela/pages/models.py` | CMS sections rendered into the homepage stack and as standalone pages. Translated fields: `title`, `content`. `slug` is a **module key** – the templates look up `page_homepage`, `page_events`, `page_music`, `page_news`, `page_gallery`, `page_bio`, `page_contact`. `position` orders parallax backgrounds (`.parallax-background-1..7`). `image` / `portrait_image` provide hero backgrounds (with mobile-portrait override). `is_dark` toggles dark-on-light styling. |
| `events.Event` | `pykapela/events/models.py` | Concerts: `title`, `datetime`, `location`, `address`, `description` (HTML), `slug`, `facebook_link`, `image`, `is_published`, `is_promoted`. Listing splits into upcoming vs. archive by `datetime` (with a 3 h grace period). |
| `social.Social` | `pykapela/social/models.py` | Social links (`name` matches CSS class `pykapela-social-<name>`, e.g. `facebook`, `instagram`, `bandzone`, `soundcloud`, `youtube`, `twitter`, `spotify`). `widget_code` is optional embed HTML rendered as `<name>_widget` in templates. `is_promoted` shows it in the hero block. |
| `menu.MenuItem` / `MenuTree` | `pykapela/menu/models.py` | The main menu, edited in admin, translated via modeltranslation. Tree alias is `main_menu`. |
| `files.File` | `pykapela/files/models.py` | Misc downloads. Per-purpose files (rider, press zip, logo) live on `Preference` instead. |
| `photologue.Gallery` / `Photo` (+ `photologue_custom`) | photologue lib + `pykapela/photologue_custom/models.py` | Image galleries. The homepage gallery strip pulls from `Preference.promoted_gallery`. |

Templates are intentionally generic: `base.html` and `index.html` pull
`config_*`, `page_*`, `socials`, `upcoming_events` and `images` from the
context that `BaseView._prepare_context()` and `WebView.index` assemble. Add
content by editing these rows in `/admin/`, not by editing templates.

## Routing model

- All public routes are wrapped in `i18n_patterns(..., prefix_default_language=PREFIX_DEFAULT_LANGUAGE)` in `pykapela/urls.py`. `PREFIX_DEFAULT_LANGUAGE` defaults to `'cs'` (Czech). Effective URLs are `/cs/...` and `/en/...`.
- The **last** urlpattern is the catch-all `^(?P<slug>.*)/$` → `PageView` which looks up a `Page` by `slug`. **Don't add new URL patterns below it** – they'll be unreachable.
- Concerts live at `/concerts/` (list) and `/concerts/<slug>/` (detail) – note both `concerts` and `^concerts/` are registered as a known historical quirk.
- Galleries: `/gallery/`, `/gallery/<slug>/`, `/gallery/photo/<slug>/`.
- 404 handler: `pykapela.pages.views.not_found_view` → `templates/404.html`.

## i18n & translations

- `LANGUAGES = [('en', …), ('cs', …)]`, `LANGUAGE_CODE = 'en-us'`, `TIME_ZONE = 'Europe/Prague'`.
- UI strings: wrap with `{% trans %}` / `gettext`. They land in `pykapela/locale/<lang>/LC_MESSAGES/django.po`.
- DB content: use modeltranslation. Register fields in `<app>/translation.py` (see `pages/translation.py`, `menu/translation.py`). Adding a translatable field requires a migration **and** a `python manage.py update_translation_fields` if data already exists.
- Adding a new language: extend `LANGUAGES`, add a `locale/<lang>/` dir, run `makemessages`, then `update_translation_fields` for modeltranslation.

## Theming & branding (per-deployment)

There is **no per-band Python code or template fork**. To rebrand:

1. Edit `Preference` (admin): `site_name`, colors, logo, favicon, custom_css, google_analytics, footer copy.
2. Create the homepage `Page` rows with the expected slugs (`homepage`, `events`, `music`, `news`, `gallery`, `bio`, `contact`) and upload hero images per page.
3. If a deployment needs heavier styling than `custom_css` can carry, add a stub theme in `pykapela/src/assets/scss/themes/<deployment>.scss` and import it from `app.scss` (currently `meteleska.scss` and `sfmagdalena.scss` exist as empty placeholders).
4. Run gulp (`yarn start` or `yarn build`) to compile to `pykapela/app/static/assets/`.

Never inline brand assets, colors or copy directly in templates / SCSS / Python.

## Build, run, deploy

Local dev:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp pykapela/settings/database.default.py pykapela/settings/database.py        # then edit
cp pykapela/settings/settings_local.default.py pykapela/settings/settings_local.py  # then edit
./manage.py migrate
./manage.py sitetreeload --mode=replace treedump.json
./manage.py collectstatic --noinput
./manage.py runserver
```

Frontend dev (separate terminal):

```bash
yarn install
yarn start          # gulp watch + browsersync proxy on :8000
yarn build          # one-shot production build
```

Deploy: `release.sh` runs `makemigrations` then `migrate`. The web process is
`gunicorn pykapela.wsgi --preload`. Static files are served by Django in dev
(`urls.py` adds explicit `serve` routes) and should be collected to
`pykapela/static/` in production.

Management commands worth knowing:
- `./manage.py seed_database` – inserts demo socials, an admin user (**dev credentials only**), and sample events. **Do not run on a real deployment.**
- `./manage.py grab_social_content` – periodic Instagram → photologue scraper (Instagram has since broken the unauthenticated endpoint; treat as legacy).
- `./manage.py sitetreeload --mode=replace treedump.json` – reload main menu fixture.

## Conventions agents must follow

1. **No hard-coded band content.** Site name, contact info, social URLs, genres, member names, track listings, concert dates, page copy, logo image, color palette – all from DB. If a feature seems to require hard-coding, add a field on `Preference` (or the matching model) instead.
2. **No band-specific template branches.** Don't write `{% if config_site_name == "Meteleska" %}`. If two deployments need to differ, expose a `Preference` flag, a new `Page` slug, or a CSS class driven by config.
3. **Pages are addressed by slug.** The templates look up `page_homepage`, `page_events`, `page_music`, `page_news`, `page_gallery`, `page_bio`, `page_contact`. New homepage modules require a new slug **plus** the matching `.parallax-background-N` CSS class (or extend the per-page loop in `base.html`).
4. **`config_*` is the bridge between DB and templates.** Adding a `Preference` field automatically exposes it as `{{ config_<column_name> }}` – no extra wiring required.
5. **Translate user-facing strings.** UI strings via `{% trans %}` / `gettext`; DB-backed content via modeltranslation – never both for the same field.
6. **Build artefacts.** SCSS / JS edits go to `pykapela/src/assets/...`; the **compiled** files in `pykapela/app/static/...` are committed (see commit history – e.g. "add compiled css") so that production deploys without a Node toolchain still ship the right assets. Always run the gulp build before committing visual changes.
7. **Settings.** Don't put deployment-specific values (secrets, hosts, S3 keys, debug flag) in `main.py`. They belong in `settings_local.py` / env vars consumed inside `database.py` / `storage.py`. Both local files are gitignored.
8. **Migrations.** Any model change (including modeltranslation fields and `Preference` new fields) needs `makemigrations` + a committed migration. `release.sh` runs migrations at deploy time.
9. **404 / handler templates** live at `pykapela/templates/404.html` – keep them content-light and DB-aware (they call `BaseView._prepare_context`).
10. **SEO / structured data.** See `SEO-AI-RESEARCH.md` for the audit and the open work items (robots.txt, sitemap.xml, JSON-LD `MusicGroup` / `MusicEvent`, hreflang, OG tags). When you add these, source the values from DB models (`Preference`, `Page`, `Event`, `Social`) – not from constants.

## Useful template variables (from `BaseView._prepare_context`)

- `SITE_NAME`, `SITE_URL`, `SITE_URL_FULL`, `CONTACT_PHONE`, `CONTACT_EMAIL` – from settings.
- `config_<field>` for every column on `Preference` (e.g. `config_logo`, `config_primary_color`, `config_google_analytics`, `config_favicon`, `config_rider_file`, `config_press_zip_file`).
- `languages`, `current_language` – language switcher data.
- `socials` – all published `Social` rows, ordered by `position`.
- `<name>_widget` – `Social` row with non-empty `widget_code`, keyed by `name` (e.g. `facebook_widget`, `twitter_widget`).
- `page_<slug>` – each published `Page`, keyed by slug.
- On the homepage: `upcoming_events`, `upcoming_events_count`, `images` (from `Preference.promoted_gallery`).

## Pointers when in doubt

- **"How does the homepage know which sections to render?"** → `WebView.index` + `BaseView._prepare_context` populate `page_<slug>` / `upcoming_events` / `images`; `templates/index.html` checks those keys.
- **"Where do menu items come from?"** → `menu.MenuTree` / `MenuItem` (django-sitetree). Edit in admin or via `treedump.json`. Rendered with `{% sitetree_menu from "main_menu" ... %}`.
- **"How do I add a new translatable field?"** → Add field on the model → register in `<app>/translation.py` → `makemigrations` → re-run `update_translation_fields` for existing rows.
- **"How do I add a new global setting (e.g. Spotify URL)?"** → New field on `Preference`, migration, then use `{{ config_<field> }}` in templates. No view changes needed.
- **"How do I add a new homepage section?"** → Create a new `Page` row with a unique slug, give it `position` + `image`, then either reuse the generic `page_<slug>` loop or add a dedicated block in `templates/index.html` + a matching `.parallax-background-N` style.

When this file goes stale, update it – it is the canonical onboarding doc for
both humans and AI agents.
