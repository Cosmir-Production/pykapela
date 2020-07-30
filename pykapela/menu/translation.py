from modeltranslation.translator import translator, TranslationOptions
from pykapela.menu.models import MenuItem


class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(MenuItem, MenuItemTranslationOptions)
