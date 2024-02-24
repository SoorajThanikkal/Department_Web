# Generated by Django 5.0.1 on 2024-02-23 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0023_remove_internalmark_marks_obtained'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totalmark',
            fields=[
                ('subject_mark', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teacher.subjectmark')),
                ('total_marks', models.FloatField(default=0.0)),
                ('total_internal_marks', models.FloatField(default=0.0)),
                ('total_sum', models.FloatField(default=0.0)),
                ('student_academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.studentacademicmodel')),
            ],
        ),
    ]
