# Generated by Django 5.0.1 on 2024-02-15 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0013_alter_computerattendancemodel_student_academic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerattendancemodel',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='computerattendancemodel',
            name='student_academic',
            field=models.ForeignKey(limit_choices_to={'sem_details__course__course_name': 'computer'}, on_delete=django.db.models.deletion.CASCADE, to='teacher.studentacademicmodel'),
        ),
    ]
