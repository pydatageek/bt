from django.contrib import admin

from .models import University, UnitPrice


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_qualifications')

    def get_qualifications(self, obj):
        return ', '.join([str(q) for q in obj.qualifications.all()])
    get_qualifications.short_description = 'Qualifications'


@admin.register(UnitPrice)
class UnitPriceAdmin(admin.ModelAdmin):
    pass
