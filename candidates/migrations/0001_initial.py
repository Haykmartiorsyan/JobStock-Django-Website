# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='candidates_images')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('profession', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('about', models.TextField(blank=True, default=None, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('web_site', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('phone_number', models.CharField(default=None, max_length=64)),
                ('location', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('facebook_profile', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('twitter_profile', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('linkedin_profile', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('google_plus_profile', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('instagram_profile', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('dr_profile', models.URLField(blank=True, default=None, max_length=64, null=True)),
                ('resume_content', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sckool_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('qualification', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='candidates.Candidates')),
            ],
            options={
                'verbose_name': 'Candidate Education',
                'verbose_name_plural': 'Candidates Educations',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('position', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='candidates.Candidates')),
            ],
            options={
                'verbose_name': 'Candidate Experience',
                'verbose_name_plural': 'Candidates Experiences',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('percent', models.IntegerField(default=1)),
                ('candidate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='candidates.Candidates')),
            ],
            options={
                'verbose_name': 'Candidate Skill',
                'verbose_name_plural': 'Candidates Skills',
            },
        ),
    ]