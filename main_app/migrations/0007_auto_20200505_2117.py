# Generated by Django 3.0.4 on 2020-05-05 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200505_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='posted_by_id',
            new_name='posted_by',
        ),
    ]