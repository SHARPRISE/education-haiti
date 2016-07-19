# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20160717_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('emitted', models.DateField()),
                ('expires', models.DateField()),
                ('completion', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='mentor',
            name='current_status',
            field=models.CharField(default='Your current status/work', max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='first_name',
            field=models.CharField(default='Your first name', max_length=100),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='grad_college',
            field=models.CharField(choices=[('1', 'Illinois State University'), ('2', 'Mount Holyoke College'), ('3', 'University of Notre Dame'), ('4', 'Columbia University'), ('5', 'Cornell University'), ('6', 'Ecole Polytechnique de Montreal'), ('7', 'Georgia Tech University'), ('8', 'Harvard University'), ('9', 'Louisiana State University'), ('10', 'Massachusettes Institute of Technology'), ('11', 'McGill University'), ('12', 'Moncton University'), ('13', 'Southern University'), ('14', 'Tufts University'), ('15', 'University of Michigan'), ('16', 'University of Pennsyvalnia'), ('17', 'Cooper Union'), ('18', 'St Leo University'), ('19', 'Stony Brook University'), ('20', 'University of Ottawa'), ('21', 'Berea College'), ('22', 'Massasoit CC'), ('23', 'University of Massachusetts'), ('24', 'University of South Florida'), ('25', 'Princeton University'), ('26', '------------------------')], default='No University', max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='interests',
            field=models.CharField(default='Your interests, please separate each one with a comma', max_length=150),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='last_name',
            field=models.CharField(default='Your last name', max_length=100),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='majors',
            field=models.CharField(default='Your major(s), please separate each major with a comma', max_length=100),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='phone',
            field=models.CharField(default='Your phone number', max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='picture',
            field=models.ImageField(blank=True, upload_to='mentor_profile_images'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='residency',
            field=models.CharField(default='Your state/city of residency', max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='school_haiti',
            field=models.CharField(default='Your school in Haiti', max_length=255),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='undergrad_college',
            field=models.CharField(choices=[('1', 'Illinois State University'), ('2', 'Mount Holyoke College'), ('3', 'University of Notre Dame'), ('4', 'Columbia University'), ('5', 'Cornell University'), ('6', 'Ecole Polytechnique de Montreal'), ('7', 'Georgia Tech University'), ('8', 'Harvard University'), ('9', 'Louisiana State University'), ('10', 'Massachusettes Institute of Technology'), ('11', 'McGill University'), ('12', 'Moncton University'), ('13', 'Southern University'), ('14', 'Tufts University'), ('15', 'University of Michigan'), ('16', 'University of Pennsyvalnia'), ('17', 'Cooper Union'), ('18', 'St Leo University'), ('19', 'Stony Brook University'), ('20', 'University of Ottawa'), ('21', 'Berea College'), ('22', 'Massasoit CC'), ('23', 'University of Massachusetts'), ('24', 'University of South Florida'), ('25', 'Princeton University'), ('26', '------------------------')], default='No University', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('A', 'mentor'), ('B', 'mentee')], default=('B', 'mentee'), max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='undergrad_college',
            field=models.CharField(choices=[('1', 'Illinois State University'), ('2', 'Mount Holyoke College'), ('3', 'University of Notre Dame'), ('4', 'Columbia University'), ('5', 'Cornell University'), ('6', 'Ecole Polytechnique de Montreal'), ('7', 'Georgia Tech University'), ('8', 'Harvard University'), ('9', 'Louisiana State University'), ('10', 'Massachusettes Institute of Technology'), ('11', 'McGill University'), ('12', 'Moncton University'), ('13', 'Southern University'), ('14', 'Tufts University'), ('15', 'University of Michigan'), ('16', 'University of Pennsyvalnia'), ('17', 'Cooper Union'), ('18', 'St Leo University'), ('19', 'Stony Brook University'), ('20', 'University of Ottawa'), ('21', 'Berea College'), ('22', 'Massasoit CC'), ('23', 'University of Massachusetts'), ('24', 'University of South Florida'), ('25', 'Princeton University'), ('26', '------------------------')], default='No University', max_length=255),
        ),
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Mentor'),
        ),
    ]