"""
Settings required in you project settings.
Please modify according to your requirements.
Usage can be found in example project.
"""

# Required paths to all locale dirs
# LOCALE_PATHS = [
#     '/foo/bar/locale',
#     '/foo/foo/bar/locale',
# ]
# THIS IS SET in settings_main.py !!!
PREFIX_DEFAULT_LANGUAGE = 'cs'

# Mode the translation manager behaves when creating
# translations mainly from multiple locale files
# Default value is N, where translation in DB are
# only once for specific locale file.
# Another option is P, where is translation manager
# promiscuous and creates for every translation it's
# instance for every locale file. It's useful, i.e.
# if you want has original system trasnlations and
# also client's custom translations
TRANSLATIONS_MODE = "P"

# For storing all translations to db regardless they have
# any occurrencies or not set True, otherwise set False.
# If False only translations having occurrencies in your
# application will be stored.
TRANSLATIONS_ALLOW_NO_OCCURRENCES = False

# Dirs and files ignored for make messages.
# TRANSLATIONS_IGNORED_PATHS = ['env', 'foo', 'bar']
TRANSLATIONS_IGNORED_PATHS = ['env']

# Backup on make messages:
TRANSLATIONS_MAKE_BACKUPS = True

# Clean .po files (delete content) after backup (this prevents duplicities)
TRANSLATIONS_CLEAN_PO_AFTER_BACKUP = True

# Forced filters on changelist queryset.
# Uses ORed original__contains Django ORM filter.
# TRANSLATIONS_QUERYSET_FORCE_FILTERS = ['foo', 'bar']
TRANSLATIONS_QUERYSET_FORCE_FILTERS = []

# Language to display in hint column to help translators
# see translation of string in another language
# TRANSLATIONS_HINT_LANGUAGE = 'foo'
TRANSLATIONS_HINT_LANGUAGE = ''

# Relative path to locale dir with hint languages
# Current locale path of translated string used by default
TRANSLATIONS_HINT_LANGUAGE_FORCED_RELATIVE_LOCALE_PATH = ''

# exclude fields from administration:
TRANSLATIONS_ADMIN_EXCLUDE_FIELDS = []

# Define admin fields manually: for all fields look to admin.py:default_fields
TRANSLATIONS_ADMIN_FIELDS = []

# Label of custom filters
TRANSLATIONS_CUSTOM_FILTERS_LABEL = ""

# List containing regex expression and label used for filtering in administration.
# Each object should be a tuple of (regex_filter, label)
TRANSLATIONS_CUSTOM_FILTERS = []

# Limits locale paths of published translations when updating POs from DB.
TRANSLATIONS_UPDATE_FORCED_LOCALE_PATHS = []

# List of django domains for translation strings.
# Defaults are ['django', 'djangojs']
TRANSLATIONS_DOMAINS = ['django', 'djangojs', 'admin', 'pykapela']

# auto create directories by translation languages
TRANSLATIONS_AUTO_CREATE_LANGUAGE_DIRS = True

# Type of translation computation running mode.
# For synchronous type 'sync' (default)
# For asynchronous type 'async_django_rq with django_rq usage
TRANSLATIONS_PROCESSING_METHOD = 'sync'

# Name of rq_queue, default is 'default'
TRANSLATIONS_PROCESSING_QUEUE = 'default'
