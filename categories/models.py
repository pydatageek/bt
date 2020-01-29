from django.db import models
from django.utils.translation import gettext_lazy as _

from _bases.models import ExamType


# Base Model for categories
class BaseModel(models.Model):
    name = models.CharField(
        _('name'), max_length=50)
    code = models.CharField(
        _('code'), max_length=25)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# Category related models
class Sector(BaseModel):
    """
        Parent of Qualification
    """
    class Meta:
        verbose_name = _('Sector')
        verbose_name_plural = _('Sectors')
        ordering = ('code',)


class Qualification(BaseModel):
    """
        Parent of Unit
    """
    sector = models.ForeignKey(
        Sector, on_delete=models.CASCADE,
        related_name='qualifications', verbose_name=_('sector'))

    class Meta:
        verbose_name = _('Qualification')
        verbose_name_plural = _('Qualifications')
        ordering = ('code',)

    # def _get_units(self, qualification):
    #     if hasattr(self, '_prefetched_objects_cache') and 'units' in self._prefetched_objects_cache:
    #         return [c for c in self._prefetched_objects_cache['units'] if c.qualification == qualification]
    #     else:
    #         return self.units.filter(qualification=qualification)


class Unit(BaseModel):
    """
        Parent of Statement(s):
                - KnowledgeStatement
                - SkillStatement
    """
    own_code = models.CharField(
        _('own code'), max_length=10)
    qualification = models.ForeignKey(
        Qualification, on_delete=models.CASCADE,
        related_name='units', verbose_name=_('qualification'))
    required = models.BooleanField(
        _('is required'),
        help_text=_('own_code prefixed by A are always required'))
    exam_types = models.ManyToManyField(
        ExamType, blank=True,
        related_name='units', verbose_name=_('exam types'))
    exam_config = models.CharField(
        _('exam config'), max_length=50,
        help_text=_('T1:60:10:60,120 means T1 exam, \
        60 limit to pass, min. 10 questions, \
        time is 60-120 sec/question'))

    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
        ordering = ('code',)


class Statement(BaseModel):
    own_code = models.CharField(
        _('own code'), max_length=10)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE,
        related_name='%(class)ss', verbose_name=_('unit'))

    class Meta:
        abstract = True
        verbose_name = _('Statement')
        verbose_name_plural = _('Statements')


class KnowledgeStatement(Statement):
    class Meta:
        verbose_name = _('Knowledge Statement')
        verbose_name_plural = _('Knowledge Statements')
        ordering = ('unit__qualification__code', 'unit', 'pk')


class SkillStatement(Statement):
    critical_step = models.BooleanField(
        _('critical step'),
        default=False)

    class Meta:
        verbose_name = _('Skill Statement')
        verbose_name_plural = _('Skill Statements')
        ordering = ('unit__qualification__code', 'unit', 'pk')
