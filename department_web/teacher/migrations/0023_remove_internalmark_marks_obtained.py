# Generated by Django 5.0.1 on 2024-02-23 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0022_alter_computerattendancemodel_date_internalmark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internalmark',
            name='marks_obtained',
        ),
    ]