# Generated by Django 2.0.5 on 2018-06-05 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prode', '0007_remove_team_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='bets',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='user',
        ),
        migrations.AddField(
            model_name='bet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bet',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bets', to='prode.Match'),
        ),
        migrations.AlterUniqueTogether(
            name='bet',
            unique_together={('user', 'match')},
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
