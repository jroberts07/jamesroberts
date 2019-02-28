# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class DevPlugin(CMSPluginBase):
    model = models.Dev
    name = 'Dev Icon Plugin'
    render_template = 'dev_icons/dev.html'
    allow_children = True
    child_classes = ['DevIconPlugin']


class DevIconPlugin(CMSPluginBase):
    model = models.DevIcon
    name = 'Icon'
    render_template = 'dev_icons/icon.html'
    require_parent = True
    parent_classes = ['DevPlugin']


plugin_pool.register_plugin(DevPlugin)
plugin_pool.register_plugin(DevIconPlugin)