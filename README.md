# pykapela

With this app, your band will obviously become world-famous.
We do not offer refunds if the avalanche of concert bookings becomes overwhelming.
Possible side effects include louder encores, shinier promo photos, and fans who suddenly know all the lyrics.

`pykapela` is a Django website template for music bands. It is built as a reusable codebase that can power multiple band websites while keeping branding, content, media, and translations in the database instead of hard-coding them into templates.

The project includes the main building blocks a band website usually needs: a homepage assembled from CMS-like sections, concert listings, galleries, social links, multilingual content, and theme customization.

## Features

- Admin-managed site settings through a single `Preference` model.
- Homepage sections backed by editable `Page` records.
- Concert listings with upcoming and archived events.
- Photo galleries powered by `django-photologue`.
- Social links and optional embedded widgets.
- Multilingual URLs and translated content.
- Theme overrides via SCSS without forking the whole project.
- Mobile friendly.

## Tech Stack

- Python `3`
- Django `3`
- PostgreSQL
- Foundation 6, Gulp, SCSS, and webpack for frontend assets
- Gunicorn for deployment

## Quick Start

Clone the repository, create a virtual environment, install the dependencies, and create local settings from the provided templates.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp pykapela/settings/database.default.py pykapela/settings/database.py
cp pykapela/settings/settings_local.default.py pykapela/settings/settings_local.py
```

Update the copied settings files for your local environment:

- `pykapela/settings/database.py` for database credentials
- `pykapela/settings/settings_local.py` for local site settings such as `SECRET_KEY`, `SITE_NAME`, `SITE_URL_FULL`, `CONTACT_EMAIL`, and `ALLOWED_HOSTS`

Create the database schema and load the base site structure:

```bash
./manage.py migrate
./manage.py createsuperuser
./manage.py sitetreeload --mode=replace treedump.json
./manage.py collectstatic --noinput
./manage.py runserver
```

Then open `http://127.0.0.1:8000/` and sign in to the admin to create your site content.

If you want sample local data, the repository also includes:

```bash
./manage.py seed_database
```

Use it for development only.

## Frontend Workflow

Frontend source files live in `pykapela/src/assets/` and compile into `pykapela/app/static/`.

Use a second terminal for asset development:

```bash
yarn install
yarn start
```

`yarn start` watches SCSS, JavaScript, and templates, then rebuilds assets into `pykapela/app/static/`.

For a one-off production build:

```bash
yarn build
```

## How Content Is Managed

This project is intentionally database-driven. A fresh clone will run, but it will not look like a finished band website until you add content in the Django admin.

The main content models are:

- `Preference`: global site settings such as site name, colors, logo, contact details, files, and homepage gallery selection
- `Page`: CMS pages and homepage sections such as `homepage`, `events`, `music`, `news`, `gallery`, `bio`, and `contact`
- `Event`: concerts with date, location, description, image, and publishing flags
- `Social`: social links and optional embed widgets
- `MenuItem` and `MenuTree`: the main navigation
- `Gallery` and `Photo`: photo galleries used across the site

Human-facing content should come from these models, not from hard-coded values in templates or Python files.

## Configuration

The Django settings are split into multiple modules and assembled in `pykapela/settings/__init__.py`.

The most important local files are:

- `pykapela/settings/database.py`: database configuration
- `pykapela/settings/settings_local.py`: deployment-specific overrides

The default local configuration templates are committed as:

- `pykapela/settings/database.default.py`
- `pykapela/settings/settings_local.default.py`

This setup keeps the shared codebase reusable across multiple deployments while allowing each site to keep its own database, media, and local settings.

## Customization

Most rebranding does not require template changes.

Typical customization flow:

1. Update the `Preference` record in the admin for site name, logo, colors, contact details, analytics, and downloadable files.
2. Create or edit the expected `Page` rows for the homepage sections.
3. Manage navigation through the menu models and `treedump.json`.
4. Add CSS overrides through `Preference.custom_css` or create a dedicated theme file in `pykapela/src/assets/scss/themes/`.
5. Rebuild frontend assets with `yarn build` when SCSS or JS changes.

If you need deployment-specific styling, import a theme stub from `pykapela/src/assets/scss/app.scss` instead of forking templates.

## Internationalization

Public routes are wrapped in Django `i18n_patterns`, so pages are served under language-prefixed URLs such as `/cs/` and `/en/`.

Translations are split across two layers:

- UI strings use Django gettext and live in `pykapela/locale/<lang>/LC_MESSAGES/django.po`
- Database-backed content uses `django-modeltranslation`

When adding a new translatable model field, you typically need:

1. a model change
2. a translation registration update
3. a migration
4. `python manage.py update_translation_fields` if existing data should be backfilled

## Project Layout

```text
manage.py
Procfile
release.sh
requirements.txt
runtime.txt
package.json
pykapela/
  settings/
  templates/
  base/
  preferences/
  pages/
  events/
  gallery/
  photologue_custom/
  menu/
  social/
  files/
  src/assets/
  app/static/
```

Two static directories matter:

- `pykapela/src/assets/` contains the source SCSS, JS, and images
- `pykapela/app/static/` contains the compiled assets committed with the project

## Deployment Notes

The repository follows a Heroku-style layout:

- `Procfile` and `release.sh` define the deployment entrypoints
- `release.sh` runs `makemigrations` and `migrate`
- the Django WSGI module lives in `pykapela.wsgi`

In development, Django also serves static and media files directly through the URL configuration.

## Useful Management Commands

- `./manage.py runserver` starts the Django development server
- `./manage.py migrate` applies database migrations
- `./manage.py collectstatic --noinput` collects static files
- `./manage.py sitetreeload --mode=replace treedump.json` loads the main menu tree
- `./manage.py seed_database` inserts demo data for local development only

## Contributing

Contributions are welcome.

When contributing:

- keep the project band-agnostic
- avoid hard-coded branding or contact details
- put SCSS and JS source changes in `pykapela/src/assets/`
- rebuild compiled assets when frontend code changes
- add migrations for any model changes

## Project Status

This is a reusable production-oriented codebase on an older Django/Python stack. If you plan to adopt it for a new site, expect some modernization work as part of setup and long-term maintenance.

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

[Creative Commons License](https://creativecommons.org/licenses/by/4.0/)