# Generated by Django 5.0.1 on 2024-02-10 08:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_studentprofile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='adm_no',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(5)]),
        ),
    ]
