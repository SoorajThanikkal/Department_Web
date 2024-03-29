# Generated by Django 5.0.1 on 2024-02-15 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0014_alter_computerattendancemodel_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerattendancemodel',
            name='student_academic',
            field=models.ForeignKey(blank=True, limit_choices_to={'sem_details__course__course_name': 'computer'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.studentacademicmodel'),
        ),
    ]
