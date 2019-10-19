from django.contrib import admin

from .models import (
    Exam, ChildExam,
    StudentExamLog, StudentQuestionLog)
from .forms import ExamForm, ChildExamForm


class ChildExamInline(admin.TabularInline):
    model = ChildExam
    form = ChildExamForm

    min_num = 2
    max_num = 4
    extra = 0


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    form = ExamForm
    inlines = (ChildExamInline,)

    list_display = ('name', 'qualification', 'date')

    def date(self, obj):
        closest_child_exam = obj.child_exams.order_by('date').first()
        return closest_child_exam.date


@admin.register(StudentExamLog)
class StudentExamLogAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentQuestionLog)
class StudentQuestionLogAdmin(admin.ModelAdmin):
    pass