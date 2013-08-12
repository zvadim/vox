from modeltranslation.translator import translator, TranslationOptions
from .models import Publication, Member, Category


class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'short_text', 'text', 'is_active',)

translator.register(Publication, PublicationTranslationOptions)


class MemberTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'about',)

translator.register(Member, MemberTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, CategoryTranslationOptions)