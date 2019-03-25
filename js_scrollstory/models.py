# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from cms.models.pluginmodel import CMSPlugin
from js_color_picker.fields import RGBColorField
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField


@python_2_unicode_compatible
class ScrollStoryContainer(CMSPlugin):
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title or str(self.pk)

    def get_id(self):
        return slugify(self.title or 'scroll story %s' % self.pk)


@python_2_unicode_compatible
class ScrollStoryImageSection(CMSPlugin):
    title = models.CharField(_('Anchor title'), max_length=255, blank=True, null=True)
    background_image = FilerImageField(verbose_name=_('Background Image'), related_name='+')
    content = HTMLField(_('Content'), default='', blank=True)
    layout = models.CharField(_('layout'), max_length=60, default='', blank=True)

    def __str__(self):
        return self.title or str(self.pk)

    def get_id(self):
        return slugify(self.title or 'story %s' % self.pk)


@python_2_unicode_compatible
class ScrollStoryColumn(CMSPlugin):
    title = models.CharField(_('Anchor title'), max_length=255, blank=True, null=True)
    background_color = RGBColorField(_('Background Color'), blank=True, null=True)
    background_image = FilerImageField(verbose_name=_('Background Image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    layout = models.CharField(_('layout'), max_length=60, default='', blank=True)

    def __str__(self):
        return self.title or str(self.pk)

    def get_id(self):
        return slugify(self.title or 'story %s' % self.pk)

