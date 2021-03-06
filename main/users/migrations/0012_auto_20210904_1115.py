# Generated by Django 3.2.7 on 2021-09-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210904_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamtask',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='usertask',
            name='completed',
        ),
        migrations.AddField(
            model_name='teamtask',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usertask',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='opuser',
            name='docs_count_plan',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
