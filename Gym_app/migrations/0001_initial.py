# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 12:55
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassInSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('class_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.ClassInformation')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('valid_through', models.DateTimeField()),
                ('security_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DietDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseInPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('repetitions', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GoalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('registrationDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MembershipCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_purchase', models.DateTimeField()),
                ('valid_through', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PartialGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('attendee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gym_app.Member')),
                ('class_in_schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gym_app.ClassInSchedule')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrainingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='DietDayTemplate',
            fields=[
                ('dietday_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Gym_app.DietDay')),
            ],
            bases=('Gym_app.dietday',),
        ),
        migrations.CreateModel(
            name='DietPlanTemplate',
            fields=[
                ('dietplan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Gym_app.models.diet_plan_models.Diet')),
            ],
            bases=('Gym_app.dietplan',),
        ),
        migrations.AddField(
            model_name='member',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gym_app.TrainingPlan'),
        ),
        migrations.AddField(
            model_name='meal',
            name='diet_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.DietDay'),
        ),
        migrations.AddField(
            model_name='groupclass',
            name='attendees',
            field=models.ManyToManyField(to='Gym_app.Member'),
        ),
        migrations.AddField(
            model_name='groupclass',
            name='class_in_schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Gym_app.ClassInSchedule'),
        ),
        migrations.AddField(
            model_name='exerciseinplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.TrainingPlan'),
        ),
        migrations.AddField(
            model_name='dietday',
            name='diet_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.models.diet_plan_models.Diet'),
        ),
        migrations.AddField(
            model_name='classinschedule',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gym_app.Instructor'),
        ),
    ]
