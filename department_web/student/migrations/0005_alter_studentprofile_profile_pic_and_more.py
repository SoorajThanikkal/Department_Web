# Generated by Django 5.0.1 on 2024-02-10 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_studentprofile_adm_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_pic',
            field=models.ImageField(default='c-3.png', null=True, upload_to='profile_photo/'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='register_no',
            field=models.PositiveIntegerField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(10)]),
        ),
    ]