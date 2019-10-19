from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from categories.models import Qualification


class User(AbstractUser):
    """
        Only employees are users.
        There are some groups
    """

    GENDERS = (
        ('F', 'Female'), ('M', 'Male'), ('N', 'Unstated'))

    gender = models.CharField(
        _('gender'), max_length=1,
        choices=GENDERS, default='N')
    id_number = models.CharField(
        _('id code'), max_length=15,
        help_text=_('unique number for a person \
        like citizen id number, passport serial etc.'))
    qualification = models.ForeignKey(
        Qualification, on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name=_('qualification'))

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
