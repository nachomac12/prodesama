# Generated by Django 2.0.4 on 2018-06-10 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0011_auto_20180609_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='end_flag',
        ),
    ]
