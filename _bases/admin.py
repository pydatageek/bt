from django.contrib import admin

from .models import ExamType

admin.site.site_header = 'BT Admin'
admin.site.site_title = 'BT Admin Portal'
admin.site.index_title = 'Welcome to BT Portal'


@admin.register(ExamType)
class ExamTypeAdmin(admin.ModelAdmin):
    pass
