from django import forms

from dal import autocomplete

from categories.forms import (
    QualificationSelectForm, UnitSelectForm,
    KnowledgeStatementSelectFrom)

from .models import KnowledgeQuestion, SkillQuestion


class KnowledgeQuestionForm(KnowledgeStatementSelectFrom):
    class Meta:
        model = KnowledgeQuestion
        fields = (
            'text', 'right_answer',
            'qualification', 'unit', 'statement')
        widgets = {
            'text': forms.Textarea(attrs={'rows':3}),
        }


class SkillQuestionForm(UnitSelectForm):
    class Meta:
        model = SkillQuestion
        fields = (
            'text', 'qualification', 'unit')
        widgets = {
            'text': forms.Textarea(attrs={'rows':3})
        }
