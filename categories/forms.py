from django import forms
from django.utils.translation import gettext_lazy as _

from dal import autocomplete

from .models import (
    Qualification, Unit,
    KnowledgeStatement, SkillStatement)


# Base forms

class QualificationSelectForm(forms.ModelForm):
    qualification = forms.ModelChoiceField(
        queryset=Qualification.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='ac_qualification'),
        help_text=_('DONE - chained selects'),
        required=False
    )


class UnitSelectForm(QualificationSelectForm):
    unit = forms.ModelChoiceField(
        queryset=Unit.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='ac_unit',
            forward=['qualification'],),
        required=False,
    )

    def get_initial_for_field(self, field, field_name):
        if self.instance.pk:
            if field_name == 'qualification':
                return self.instance.unit.qualification

        return super().get_initial_for_field(field, field_name)


class UnitMultiSelectForm(QualificationSelectForm):
    units = forms.ModelMultipleChoiceField(
        queryset=Unit.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='ac_unit',
            forward=['qualification']),
        required=False,
    )

    past_units = forms.ModelMultipleChoiceField(
        queryset=Unit.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='ac_unit',
            forward=['qualification']),
        required=False,
        help_text=_('TODO: to be seen ONLY if apply_reason is Unit Binding. \
            units and past_units cannot contain same objects')
    )


class KnowledgeStatementSelectFrom(UnitSelectForm):
    statement = forms.ModelChoiceField(
        queryset=KnowledgeStatement.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='ac_ks',
            forward=['unit']),
    )

    def get_initial_for_field(self, field, field_name):
        if self.instance.pk:
            if field_name == 'qualification':
                return self.instance.statement.unit.qualification
            if field_name == 'unit':
                return self.instance.statement.unit

        return super().get_initial_for_field(field, field_name)


class StatementForm(UnitSelectForm):
    pass


# app related forms

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
