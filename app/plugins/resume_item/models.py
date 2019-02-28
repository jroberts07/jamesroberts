# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin


@python_2_unicode_compatible
class ResumeItem(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )
    header = models.CharField(
        blank=True,
        max_length=200,
    )
    sub_header = models.CharField(
        blank=True,
        max_length=200,
    )
    information = models.CharField(
        blank=True,
        max_length=1000,
    )
    date = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label