# Generated by Django 3.2.7 on 2021-09-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210903_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
