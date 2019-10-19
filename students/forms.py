from django import forms

from dal import autocomplete

from categories.forms import UnitMultiSelectForm

from .models import Student


class StudentForm(UnitMultiSelectForm):
    class Meta:
        model = Student
        fields = '__all__'
