from django import forms

from dal import autocomplete

from categories.forms import QualificationSelectForm
from students.models import Student

from .models import Exam, ChildExam


class ExamForm(QualificationSelectForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='ac_student',
            forward=['qualification']),
    )

    class Meta:
        model = Exam
        fields = '__all__'


class ChildExamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # TODO: all exams must have 2 childexams
        # with exam type T1 and P1 so they should
        # be added as inline automatically
        super().__init__(*args, **kwargs)


    class Meta:
        model = ChildExam
        fields = '__all__'
