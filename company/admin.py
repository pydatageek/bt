from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    def has_add_permission(self, *args, **kwargs):
        """There should be only one company!"""
        return not Company.objects.exists()
