# Generated by Django 3.2.7 on 2021-09-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210904_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docstatus',
            name='time_end',
        ),
        migrations.AddField(
            model_name='docstatus',
            name='day_end',
            field=models.IntegerField(blank=True, default=4),
        ),
    ]
