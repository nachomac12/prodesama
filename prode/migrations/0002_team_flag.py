# Generated by Django 2.0.4 on 2018-05-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='flag',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
