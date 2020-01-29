from django.contrib import admin
from django.db.models import Count

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

    def get_queryset(self, request):
        """
          Total counts are taken with this get_queryset method.
          There are no per object extra queries.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _qualifications_count=Count('qualifications', distinct=True)
        )
        return queryset

    def qualifications_count(self, obj):
        return obj._qualifications_count
    qualifications_count.short_description = '# Qualifications'
    qualifications_count.admin_order_field = '_qualifications_count'


@admin.register(Qualification)
class QualificationAdmin(ImportExportModelAdmin):
    resource_class = QualificationResource

    search_fields = ('name',)
    list_filter = (
        ('sector', admin.RelatedOnlyFieldListFilter),)

    list_select_related = ('sector',)
    list_display = ('code', 'name', 'sector', 'units_count')

    autocomplete_fields = ('sector',)

    def get_queryset(self, request):
        """
          Total counts are taken with this get_queryset method.
          There are no per object extra queries.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _units_count=Count('units', distinct=True)
        )
        return queryset

    def units_count(self, obj):
        return obj._units_count
    units_count.short_description = '# Units'
    units_count.admin_order_field = '_units_count'


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

    def get_queryset(self, request):
        """
          Total counts are taken with this get_queryset method.
          There are no per object extra queries.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _ks_count=Count('knowledgestatements', distinct=True),
            _ss_count=Count('skillstatements', distinct=True)
        )
        return queryset

    def knowledge_statements_count(self, obj):
        return obj._ks_count
    knowledge_statements_count.short_description = '# Knowledge Statements'
    knowledge_statements_count.admin_order_field = '_ks_count'

    def skill_statements_count(self, obj):
        return obj._ss_count
    skill_statements_count.short_description = '# Skill Statements'
    skill_statements_count.admin_order_field = '_ss_count'


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

    def get_queryset(self, request):
        """
          Total counts are taken with this get_queryset method.
          There are no per object extra queries.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _questions_count=Count('questions', distinct=True),
        )
        return queryset

    def questions_count(self, obj):
        return obj._questions_count
    questions_count.short_description = '# Questions'
    questions_count.admin_order_field = '_questions_count'


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
