# Generated by Django 5.0.1 on 2024-02-15 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0016_alter_computerattendancemodel_student_academic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerattendancemodel',
            name='student_academic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.studentacademicmodel'),
        ),
    ]