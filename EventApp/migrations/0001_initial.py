# Generated by Django 2.1.3 on 2018-11-17 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EventDepartment',
            fields=[
                ('event_dep_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventApp.Department')),
            ],
        ),
        migrations.CreateModel(
            name='EventMaster',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('num_of_winners', models.IntegerField()),
                ('team_size', models.IntegerField()),
                ('entry_fee', models.IntegerField()),
                ('rules', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='eventdepartment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventApp.EventMaster'),
        ),
    ]
