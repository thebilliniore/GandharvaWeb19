# Generated by Django 2.1.3 on 2018-11-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0002_auto_20181118_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdepartment',
            name='event_dep_id',
        ),
        migrations.AddField(
            model_name='eventdepartment',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
