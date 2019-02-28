# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ResumeMainInfoPlugin(CMSPluginBase):
    model = models.ResumeMainInfo
    name = 'Resume Main Info Plugin'
    render_template = 'resume_main_info/info.html'


plugin_pool.register_plugin(ResumeMainInfoPlugin)