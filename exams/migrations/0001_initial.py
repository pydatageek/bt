# Generated by Django 2.2.6 on 2019-10-16 22:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('questions', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('T1', 'T1'), ('T2', 'T2'), ('P1', 'P1'), ('P2', 'P2')], max_length=2, verbose_name='exam type')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
            ],
            options={
                'verbose_name': 'child exam',
                'verbose_name_plural': 'child exams',
            },
        ),
        migrations.CreateModel(
            name='StudentQuestionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_question_logs', to='exams.ChildExam', verbose_name='child exam')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_question_logs', to='questions.Question', verbose_name='question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_question_logs', to='students.Student', verbose_name='student')),
            ],
            options={
                'verbose_name': 'Student Exam Question Log',
                'verbose_name_plural': 'Student Exam Question Logs',
                'unique_together': {('student', 'question')},
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams', to='categories.Qualification', verbose_name='qualification')),
                ('students', models.ManyToManyField(related_name='exams', to='students.Student', verbose_name='students')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
            },
        ),
        migrations.AddField(
            model_name='childexam',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_exams', to='exams.Exam', verbose_name='exam'),
        ),
        migrations.AddField(
            model_name='childexam',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='child_exams', through='exams.StudentQuestionLog', to='questions.Question', verbose_name='questions'),
        ),
        migrations.CreateModel(
            name='StudentExamLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('S', 'Satisfactory'), ('U', 'Unsatisfactory'), ('N', 'Not Attended')], default='', max_length=2, null=True, verbose_name='result')),
                ('child_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_exam_logs', to='exams.ChildExam', verbose_name='child exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_exam_logs', to='students.Student', verbose_name='student')),
                ('units', models.ManyToManyField(related_name='studentexamlogs', to='categories.Unit', verbose_name='units')),
            ],
            options={
                'verbose_name': 'Student Exam Log',
                'verbose_name_plural': 'Student Exam Logs',
                'unique_together': {('child_exam', 'student')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='childexam',
            unique_together={('exam', 'exam_type')},
        ),
    ]