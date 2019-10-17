from django.db import models
from django.utils.translation import gettext_lazy as _


# T1: Theoretical, T2: Interview
# P1 and P2: Performance
# An exam has at least two ChildExams: T1 and P1
# Child Exams are done on different days on different salloons
EXAM_TYPES = (
    ('T1', 'T1'), ('T2', 'T2'),
    ('P1', 'P1'), ('P2', 'P2'))
EXAM_TYPES_SHORT = (
    ('T', _('Theoretical')), ('P', _('Performance')),
    ('I', _('Interview')))


class ExamType(models.Model):
    name = models.CharField(
        _('name'),
        unique=True, max_length=2, choices=EXAM_TYPES)

    class Meta:
        verbose_name = _('Exam type')
        verbose_name_plural = _('Exam types')
        ordering = ('pk',)

    def __str__(self):
        return self.name
