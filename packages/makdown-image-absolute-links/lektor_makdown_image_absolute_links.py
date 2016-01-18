# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin

from lektor.context import get_ctx
from werkzeug.urls import url_parse


class ImageAbsoluteLinksMixin(object):
    def image(self, src, title, text):
        if self.record is not None:
            url = url_parse(src)
            if not url.scheme:
                src = self.record.url_to('!' + src,
                                         base_url=get_ctx().base_url)
        return super(ImageAbsoluteLinksMixin, self).image(src, title, text)


class MakdownImageAbsoluteLinksPlugin(Plugin):
    name = u'Makdown image absolute links'
    description = u'Use absolute urls to images in markdown fields.'

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(ImageAbsoluteLinksMixin)
