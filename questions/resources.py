from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from categories.models import (
    Unit, KnowledgeStatement, SkillStatement)

from .models import (
    Choice, Question,
    KnowledgeQuestion, SkillQuestion)


class KnowledgeQuestionResource(resources.ModelResource):
    statement = fields.Field(
        column_name='statement',
        attribute='statement',
        widget=ForeignKeyWidget(KnowledgeStatement, 'code')
    )

    class Meta:
        model = KnowledgeQuestion


class SkillQuestionResource(resources.ModelResource):
    unit = fields.Field(
        column_name='unit',
        attribute='unit',
        widget=ForeignKeyWidget(Unit, 'code')
    )

    class Meta:
        model = SkillQuestion


class ChoiceResource(resources.ModelResource):
    question = fields.Field(
        attribute='question',
        column_name='question',
        widget=ForeignKeyWidget(Question, 'pk')
    )

    class Meta:
        model = Choice
