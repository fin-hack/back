# Generated by Django 3.2.7 on 2021-09-03 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opuser',
            name='team',
        ),
        migrations.AddField(
            model_name='opuser',
            name='_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.team'),
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.opuser'),
            preserve_default=False,
        ),
    ]