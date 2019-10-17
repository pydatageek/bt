from django import forms
from django.forms import ModelForm

from .models import ChildExam


class ChildExamForm(ModelForm):
    def __init__(self, obj=None, *args, **kwargs):
        initial = kwargs.pop('initial', {})
        initial['exam_type'] = initial.get('exam_type', 'T1')
        kwargs['initial'] = initial
        super().__init__(obj, *args, **kwargs)

    def clean_exam_type(self):

        return self.cleaned_data['exam_type']

    class Meta:
        model = ChildExam
        fields = '__all__'
