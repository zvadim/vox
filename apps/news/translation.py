from modeltranslation.translator import translator, TranslationOptions
from .models import Publication


class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'short_text', 'text', 'is_active',)

translator.register(Publication, PublicationTranslationOptions)