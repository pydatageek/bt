from django.contrib import admin

from .models import ExamType


@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    pass
