from django import forms
from django.forms import ModelForm

from categories.forms import (
    QualificationSelectForm, UnitSelectForm)

from .models import KnowledgeQuestion, SkillQuestion


class KnowledgeQuestionForm(UnitSelectForm):
    class Meta:
        model = KnowledgeQuestion
        fields = (
            'text', 'right_answer',
            'qualification', 'unit', 'statement')
        widgets = {
            'text': forms.Textarea(attrs={'rows':3})
        }


class SkillQuestionForm(QualificationSelectForm):
    class Meta:
        model = SkillQuestion
        fields = (
            'text', 'qualification', 'unit')
        widgets = {
            'text': forms.Textarea(attrs={'rows':3})
        }
