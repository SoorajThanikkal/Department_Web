# Generated by Django 5.0.1 on 2024-02-14 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_delete_departmentclass'),
        ('teacher', '0003_alter_semester_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAcademicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.OneToOneField(limit_choices_to=models.Q(('is_student', True)), on_delete=django.db.models.deletion.CASCADE, to='public.register')),
            ],
        ),
    ]
