# Generated by Django 3.0.8 on 2021-06-06 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_auto_20210606_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuschedule',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu_app.Menu'),
        ),
    ]