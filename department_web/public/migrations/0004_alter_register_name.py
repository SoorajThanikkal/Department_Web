# Generated by Django 5.0.1 on 2024-02-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_alter_register_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
