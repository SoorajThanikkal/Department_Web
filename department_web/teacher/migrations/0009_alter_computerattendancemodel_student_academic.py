# Generated by Django 5.0.1 on 2024-02-15 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_computerattendancemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerattendancemodel',
            name='student_academic',
            field=models.ForeignKey(limit_choices_to=models.Q(('sem_details__course', 'computer')), on_delete=django.db.models.deletion.CASCADE, to='teacher.studentacademicmodel'),
        ),
    ]