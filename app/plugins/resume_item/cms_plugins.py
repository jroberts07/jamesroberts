# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ResumeItemPlugin(CMSPluginBase):
    model = models.ResumeItem
    name = 'Resume Item Plugin'
    render_template = 'resume_item/item.html'


plugin_pool.register_plugin(ResumeItemPlugin)