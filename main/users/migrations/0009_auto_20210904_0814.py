# Generated by Django 3.2.7 on 2021-09-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210904_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opuser',
            name='attention',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opuser',
            name='docs_count',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opuser',
            name='immersion',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opuser',
            name='stress_tolerance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
