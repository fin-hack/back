# Generated by Django 3.2.7 on 2021-09-04 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210904_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='opuser',
            name='docs_count_plan',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='DocStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_end', models.TimeField(blank=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='users.opuser')),
            ],
        ),
    ]