from django.db import models
from django.utils.translation import gettext_lazy as _

from categories.models import (
    Qualification, Unit, KnowledgeStatement, SkillStatement)

LABELS = (
    ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class Question(models.Model):
    """
        TODO: check for at least 3 questions
            per statement!
        Every statement should have at least
            3 corresponding questions. WHY?
        A student has 2 make-up exam rights if s/he fails
            (3 exams in total). And any question shouldn't
            be asked to a student twice.
        TODO: warn if there is no avaliable question
            for a student to ask.
        TODO: auto check! right answer label and one of
            choice's label should match!
        TODO: All questions and choices would be randomly
            sorted for each student.
    """
    text = models.CharField(
        _('question'), max_length=250)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.text


class KnowledgeQuestion(Question):
    right_answer = models.CharField(
        _('right answer label'), max_length=1, choices=LABELS,
        help_text=_("right label and one of choice's label \
                    should match!"))
    statement = models.ForeignKey(
            KnowledgeStatement, on_delete=models.SET_NULL,
            blank=True, null=True,
            related_name='questions', verbose_name=_('knowledge statement'),
            help_text=_('qualification and unit selects are needed to reach statement'))

    class Meta:
        verbose_name = _('Knowledge Question')
        verbose_name_plural = _('Knowledge Questions')


class SkillQuestion(Question):
    """
        Exam is done with one question per unit.
        Those exam are done as workshops with unit's all skill statements
        to be included in the question.
    """
    unit = models.ForeignKey(
            Unit, on_delete=models.SET_NULL,
            blank=True, null=True,
            related_name='questions', verbose_name=_('unit'),
            help_text=_('qualification selects is needed to reach unit'))

    class Meta:
        verbose_name = _('Skill Question')
        verbose_name_plural = _('Skill Questions')


class Choice(models.Model):
    """
        If there is one choice it is True/False or Fill question
        TODO: T/F and Fill questions choices
            won't be shown to students.
    """
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='choices', verbose_name=_('question'))
    text = models.CharField(
        _('answer'), max_length=250)
    label = models.CharField(
        _('label'), max_length=1, choices=LABELS)

    class Meta:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')
        unique_together = ('question', 'label')

    def __str__(self):
        return self.text
