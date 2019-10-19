from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Student
from .forms import StudentForm
from .resources import StudentResource


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    form = StudentForm
    resource_class = StudentResource

    search_fields = ('first_name', 'last_name', 'id_number')
    list_filter = (
        'apply_reason', 'gender',
        ('qualification', admin.RelatedOnlyFieldListFilter),
        ('units', admin.RelatedOnlyFieldListFilter)
    )

    list_select_related = ('qualification',)
    list_display = (
        'id_number', 'full_name', 'apply_reason',
        'gender', 'qualification')
    list_display_links = ('full_name',)

    autocomplete_fields = (
        'qualification', 'units', 'past_units')

    suit_form_tabs = (
        ('application', 'Application'),
        ('personal', 'Personal Info'),
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-application'),
            'fields': (
                'apply_reason', 'qualification',
                'units', 'past_units')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-personal'),
            'fields': (
                'id_number', ('first_name', 'last_name'),
                'gender')
        })
    )
