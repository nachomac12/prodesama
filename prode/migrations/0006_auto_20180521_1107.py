# Generated by Django 2.0.5 on 2018-05-21 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0005_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='bets',
        ),
        migrations.AddField(
            model_name='userdata',
            name='bets',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='prode.Bet'),
            preserve_default=False,
        ),
    ]
