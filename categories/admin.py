from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import (
    Sector, Qualification, Unit,
    KnowledgeStatement, SkillStatement)
from .forms import (
    KnowledgeStatementForm, SkillStatementForm)
from .resources import (
    SectorResource, QualificationResource, UnitResource,
    KnowledgeStatementResource, SkillStatementResource)


@admin.register(Sector)
class SectorAdmin(ImportExportModelAdmin):
    # TODO: link_select_related for child models?
    resource_class = SectorResource

    search_fields = ('name',)
    list_display = ('code', 'name', 'qualifications_count')

    def qualifications_count(self, obj):
        return obj.qualifications.count()


@admin.register(Qualification)
class QualificationAdmin(ImportExportModelAdmin):
    resource_class = QualificationResource

    search_fields = ('name',)
    list_filter = (
        ('sector', admin.RelatedOnlyFieldListFilter),)

    list_select_related = ('sector',)
    list_display = ('code', 'name', 'sector', 'units_count')

    autocomplete_fields = ('sector',)

    def units_count(self, obj):
        return obj.units.count()


@admin.register(Unit)
class UnitAdmin(ImportExportModelAdmin):
    resource_class = UnitResource

    search_fields = ('name',)
    list_filter = (
        ('qualification', admin.RelatedOnlyFieldListFilter),
        ('exam_types', admin.RelatedOnlyFieldListFilter))

    list_select_related = ('qualification',)
    list_display = (
        'code', 'own_code', 'name', 'qualification',
        'knowledge_statements_count', 'skill_statements_count')

    autocomplete_fields = ('qualification',)

    def knowledge_statements_count(self, obj):
        return obj.knowledgestatements.count()

    def skill_statements_count(self, obj):
        return obj.skillstatements.count()


@admin.register(KnowledgeStatement)
class KnowledgeStatementAdmin(ImportExportModelAdmin):
    form = KnowledgeStatementForm
    resource_class = KnowledgeStatementResource

    search_fields = ('name',)
    list_filter = (
        ('unit__qualification', admin.RelatedOnlyFieldListFilter),
        ('unit', admin.RelatedOnlyFieldListFilter))

    list_select_related = ('unit', 'unit__qualification')
    list_display = (
        'code', 'own_code', 'name', 'unit', 'questions_count')

    autocomplete_fields = ('unit',)

    def questions_count(self, obj):
        return obj.questions.count()


@admin.register(SkillStatement)
class SkillStatementAdmin(ImportExportModelAdmin):
    form = SkillStatementForm
    resource_class = SkillStatementResource

    search_fields = ('name',)
    list_filter = (
        ('unit__qualification', admin.RelatedOnlyFieldListFilter),
        ('unit', admin.RelatedOnlyFieldListFilter))

    list_select_related = ('unit', 'unit__qualification')
    list_display = (
        'code', 'own_code', 'name', 'unit')

    autocomplete_fields = ('unit',)
