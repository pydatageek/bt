from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    Choice, KnowledgeQuestion, SkillQuestion)
from .forms import (
    KnowledgeQuestionForm, SkillQuestionForm)
from .resources import (
    ChoiceResource,
    KnowledgeQuestionResource, SkillQuestionResource)


class ChoiceInline(admin.TabularInline):
    model = Choice

    extra = 0
    max_num = 4


@admin.register(KnowledgeQuestion)
class KnowledgeQuestionAdmin(ImportExportModelAdmin):
    form = KnowledgeQuestionForm
    resource_class = KnowledgeQuestionResource
    inlines = (ChoiceInline,)

    search_fields = ('text',)
    list_filter = (
        # ('statement__unit__qualification', admin.RelatedOnlyFieldListFilter),
        # ('statement__unit', admin.RelatedOnlyFieldListFilter),
        ('statement', admin.RelatedOnlyFieldListFilter),)

    list_select_related = (
        'statement__unit__qualification',
        'statement__unit', 'statement')

    list_display = (
        'pk', 'text', 'qualification', 'unit',
        'statement_own_code', 'right_answer')

    autocomplete_fields = ('statement',)

    def qualification(self, obj):
        return obj.statement.unit.qualification

    def unit(self, obj):
        return obj.statement.unit

    def statement_own_code(self, obj):
        return obj.statement.own_code


@admin.register(SkillQuestion)
class SkillQuestionAdmin(ImportExportModelAdmin):
    form = SkillQuestionForm
    resource_class = SkillQuestionResource

    search_fields = ('text',)
    list_filter = (
        # ('statement__unit__qualification', admin.RelatedOnlyFieldListFilter),
        # ('statement__unit', admin.RelatedOnlyFieldListFilter),
        ('unit', admin.RelatedOnlyFieldListFilter),)

    list_select_related = ('unit__qualification', 'unit',)

    list_display = ('pk', 'text', 'qualification', 'unit')

    autocomplete_fields = ('unit',)

    def qualification(self, obj):
        return obj.unit.qualification


@admin.register(Choice)
class ChoiceAdmin(ImportExportModelAdmin):
    resource_class = ChoiceResource

    search_fields = ('text',)

    list_display = ('text', 'label')
