from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BUserAdmin, ):
    pass