# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ResumeSectionPlugin(CMSPluginBase):
    model = models.ResumeSection
    name = 'Resume Section Plugin'
    render_template = 'resume_section/section.html'
    allow_children = True


plugin_pool.register_plugin(ResumeSectionPlugin)