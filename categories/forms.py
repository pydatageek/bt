from django import forms
from django.forms import ModelForm

from .models import (
    Qualification, Unit,
    KnowledgeStatement, SkillStatement)


class QualificationSelectForm(ModelForm):
    qualification = forms.ModelChoiceField(
        queryset=Qualification.objects.all(),
        required=False,
    )


class UnitSelectForm(QualificationSelectForm):
    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        required=False,
    )


class StatementForm(QualificationSelectForm):
    qualification = forms.ModelChoiceField(
        queryset=Qualification.objects.all(),
    )


class KnowledgeStatementForm(StatementForm):
    class Meta:
        model = KnowledgeStatement
        fields = (
            'name', 'code', 'own_code',
            'qualification', 'unit')


class SkillStatementForm(StatementForm):
    class Meta:
        model = SkillStatement
        fields = (
            'name', 'code', 'own_code',
            'qualification', 'unit')
