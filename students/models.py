from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import Qualification, Unit


class Student(models.Model):
    """
        Same person can be added many times
    """
    GENDERS = (
        ('F', 'Female'), ('M', 'Male'), ('N', 'Unstated'))
    APPLY_REASONS = (
        ('FA', _('First application')),
        ('UB', _('Unit binding')),
        ('NC', _('New certificate')),
    )

    apply_reason = models.CharField(
        _('application reason'),
        max_length=2, choices=APPLY_REASONS)

    id_number = models.CharField(
        _('id code'), max_length=15,
        help_text=_('unique number for a person \
        like citizen id number, passport serial etc.'))
    first_name = models.CharField(
        _('first name'), max_length=50)
    last_name = models.CharField(
        _('last name'), max_length=50)
    gender = models.CharField(
        _('gender'),
        max_length=1, choices=GENDERS, default='N')

    qualification = models.ForeignKey(
        Qualification, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='students', verbose_name=_('qualification'))

    # TODO: check
    # required units (own_code prefixed by A) are mandatory and
    # also at least one of B units must be choosen.
    # if apply_reason is NOT UB, mandatory fields should be
    # selected automatically! because in this case student will not
    # take past units' exams.
    units = models.ManyToManyField(
        Unit, blank=True,
        related_name='students', verbose_name=_('units'))

    # TODO: to be seen when only apply_reason is UB
    # javascript be best
    past_units = models.ManyToManyField(
        Unit, blank=True,
        related_name='students_pasts', verbose_name=_('past units'))

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
