# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-16 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='resume_section_resumesection', serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(blank=True, max_length=200)),
                ('extra_classes', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
