from modeltranslation.translator import translator, TranslationOptions
from .models import Page, ClientQuote


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'short_text', 'text', 'is_active',)

translator.register(Page, PageTranslationOptions)


class ClientQuoteTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'is_active',)

translator.register(ClientQuote, ClientQuoteTranslationOptions)