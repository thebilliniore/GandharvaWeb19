# Generated by Django 2.1.3 on 2018-11-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventApp', '0006_auto_20181119_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='sponsormaster',
            name='sponsor_id',
        ),
        migrations.AddField(
            model_name='categories',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsormaster',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
