from django.db import models
from django.db.models import Exists, Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from categories.models import Qualification
from questions.models import Question
from students.models import Student

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
STUDENT_EXAM_STATUS = (
    ('S', _('Satisfactory')), ('U', _('Unsatisfactory')),
    ('N', _('Not Attended')))


class Exam(models.Model):
    """
        An exam can be on only one qualification.
        And Students only with the same qualification
            can take the exam. TODO: list only those students,
            whose qualifications match and need to take the exam
            to be certified.

    """
    name = models.CharField(
        _('name'), max_length=50)
    qualification = models.ForeignKey(
        Qualification, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='exams', verbose_name=_('qualification'),
        help_text=_('TODO: qualification and students are chained selects. \
            qualification = student.qualification'))
    students = models.ManyToManyField(
        Student,
        related_name='exams', verbose_name=_('students'),
        help_text=_('TODO: other than chained select with qualification, \
        only students who should take the exam be listed.'))

    class Meta:
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')

    def __str__(self):
        return self.name


class ChildExam(models.Model):
    """
        TODO: auto add two children (T1 and P1)
        For any exam, there should be at least 2 Child Exams
            One for T1 and the other one for P1
        If any unit of exam qualification has T2 or P2 exams
            they should be added automatically also.

        'A' prefixed units have T1 exams only, 'B' prefixed ones
            have T1, P1 and may be T2 or P2.
        Student X may have choosen 3 units: A1, B1, B2
            so s/he would take 3 T1 exams and 2 P1 exams.
        Student Y has 2 units: A1 and B1
            so s/he would take 2 T1 exams and 1 P1 exam.

    """
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE,
        related_name='child_exams', verbose_name=_('exam'))
    exam_type = models.CharField(
        _('exam type'), max_length=2,
        choices=EXAM_TYPES)
    date = models.DateTimeField(
        _('date'), default=timezone.now)

    # questions should be auto filled per student and exam!
    # on intermediate table
    questions = models.ManyToManyField(
        Question, blank=True, through='StudentQuestionLog',
        related_name='child_exams', verbose_name=_('questions'))

    class Meta:
        verbose_name = _('child exam')
        verbose_name_plural = _('child exams')
        unique_together = ('exam', 'exam_type')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for student in self.exam.students.all():
            print('Hello1')
            # if not self._state.adding:
            if StudentExamLog.objects.filter(
                    Q(child_exam=self)).filter(Q(student=student)) is None:
                print('Hello2')
                sel = StudentExamLog.objects.create(
                    child_exam=self,
                    student=student)
                for unit in student.units.all():
                    sel.units.add(unit)


class StudentExamLog(models.Model):
    child_exam = models.ForeignKey(
        ChildExam, on_delete=models.SET_NULL, null=True,
        related_name='student_exam_logs', verbose_name=_('child exam'))
    units = models.ManyToManyField(
        'categories.Unit',
        related_name='student_exam_logs', verbose_name=_('units'))
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='student_exam_logs', verbose_name=_('student'))
    result = models.CharField(
        _('result'), max_length=2,
        choices=STUDENT_EXAM_STATUS, blank=True, null=True)

    class Meta:
        verbose_name = _('Student Exam Log')
        verbose_name_plural = _('Student Exam Logs')

        # if StudentExamLogs -> result is not N
        unique_together = ('child_exam', 'student')


class StudentQuestionLog(models.Model):
    """
        This models logs the asked questions to a student

    """
    child_exam = models.ForeignKey(
        ChildExam, on_delete=models.SET_NULL, null=True,
        related_name='student_question_logs', verbose_name=_('child exam'))
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE,
        related_name='student_question_logs', verbose_name=_('student'))

    # if child_exam -> exam_type is T: Knowloedge Question
    #                               P: Skill Question
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True,
        related_name='student_question_logs', verbose_name=_('question'))

    class Meta:
        verbose_name = _('Student Exam Question Log')
        verbose_name_plural = _('Student Exam Question Logs')
        unique_together = ('student', 'question')  # if StudentExamLogs -> result is not N
