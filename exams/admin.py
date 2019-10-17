from django.contrib import admin

from .models import Exam, ChildExam
from .forms import ChildExamForm


class ChildExamInline(admin.TabularInline):
    model = ChildExam
    form = ChildExamForm

    min_num = 2
    max_num = 4
    extra = 0


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = (ChildExamInline,)

    autocomplete_fields = ('qualification', 'students')
