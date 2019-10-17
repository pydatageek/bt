from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BasesConfig(AppConfig):
    name = '_bases'
    verbose_name = _('Base Models')
