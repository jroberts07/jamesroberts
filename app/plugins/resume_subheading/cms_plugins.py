# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ResumeSubheadingPlugin(CMSPluginBase):
    model = models.ResumeSubheading
    name = 'Resume Subheading Plugin'
    render_template = 'resume_subheading/subheading.html'


plugin_pool.register_plugin(ResumeSubheadingPlugin)