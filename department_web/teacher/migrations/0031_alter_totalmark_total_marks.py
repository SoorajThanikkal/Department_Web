# Generated by Django 5.0.1 on 2024-02-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0030_rename_total_sum_totalmark_total_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalmark',
            name='total_marks',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]