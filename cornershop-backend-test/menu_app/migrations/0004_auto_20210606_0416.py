# Generated by Django 3.0.8 on 2021-06-06 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0003_auto_20210606_0403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuschedule',
            old_name='menu',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='userschoice',
            old_name='scheduled_menu',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='userschoice',
            old_name='user',
            new_name='email',
        ),
    ]
