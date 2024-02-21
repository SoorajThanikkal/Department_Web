# Generated by Django 5.0.1 on 2024-02-10 08:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_studentprofile_adm_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='adm_no',
            field=models.PositiveIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='register_no',
            field=models.PositiveIntegerField(default=0, null=True, unique=True, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]
