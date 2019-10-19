from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BUserAdmin):
    readonly_fields = ('last_login', 'date_joined')
    autocomplete_fields = ('qualification',)

    suit_form_tabs = (
        ('personal', _('Personal Info')),
        ('permission', _('Permissions')),
        ('qualification', _('Qualification')),
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-personal'),
            'fields': (
                'username',  # change password link
                ('first_name', 'last_name'), 'id_number',
                'gender',
        )}),
        (_('Permissions'), {
            'classes': ('suit-tab', 'suit-tab-permission'),
            'fields': (
                'is_active', 'groups', 'is_staff', 'is_superuser',
                'last_login', 'date_joined'
                ),  # , 'user_permissions'
            'description': (_('IMPORTANT! Assign personnel to appropriate groups'))
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-qualification'),
            'fields': (
                'qualification',
        )}),
    )