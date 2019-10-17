from import_export import fields, resources
from import_export.widgets import (
    ForeignKeyWidget, ManyToManyWidget)

from _bases.models import ExamType

from .models import (
    Sector, Qualification, Unit,
    KnowledgeStatement, SkillStatement)


class SectorResource(resources.ModelResource):
    class Meta:
        model = Sector


class QualificationResource(resources.ModelResource):
    sector = fields.Field(
        attribute='sector',
        column_name='sector',
        widget=ForeignKeyWidget(Sector, 'code')
    )

    class Meta:
        model = Qualification


class UnitResource(resources.ModelResource):
    qualification = fields.Field(
        attribute='qualification',
        column_name='qualification',
        widget=ForeignKeyWidget(Qualification, 'code')
    )
    exam_types = fields.Field(
        attribute='exam_types',
        column_name='exam_types',
        widget=ManyToManyWidget(
            ExamType, separator=',', field='name')
    )

    class Meta:
        model = Unit


class StatementResource(resources.ModelResource):
    unit = fields.Field(
        attribute='unit',
        column_name='unit',
        widget=ForeignKeyWidget(Unit, 'code')
    )

    class Meta:
        abstract = True

class KnowledgeStatementResource(StatementResource):
    class Meta:
        model = KnowledgeStatement


class SkillStatementResource(StatementResource):
    class Meta:
        model = SkillStatement
