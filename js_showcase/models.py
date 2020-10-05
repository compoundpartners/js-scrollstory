# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from cms.models.pluginmodel import CMSPlugin
from js_color_picker.fields import RGBColorField
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_attributes_field import fields

from .constants import DEVICE_SIZES


class AttributesField(fields.AttributesField):
    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = _('Attributes')
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        super(AttributesField, self).__init__(*args, **kwargs)


@python_2_unicode_compatible
class ShowcaseContainer(CMSPlugin):
    title = models.CharField(_('title'), max_length=255, blank=True, null=True)
    attributes = AttributesField()

    def __str__(self):
        return self.title or str(self.pk)

    def get_id(self):
        return slugify(self.title or 'show case %s' % self.pk)


@python_2_unicode_compatible
class ShowcaseArticle(CMSPlugin):
    title = models.CharField(_('title'), max_length=255)
    layout = models.CharField(_('layout'), max_length=60, default='', blank=True)
    attributes = AttributesField()

    def __str__(self):
        return self.title

    def get_id(self):
        return slugify(self.title)


@python_2_unicode_compatible
class ShowcaseSection(CMSPlugin):
    title = models.CharField(_('Anchor title'), max_length=255, blank=True, null=True)
    background_color = RGBColorField(_('Background Color'), blank=True, null=True)
    background_image = FilerImageField(verbose_name=_('Background Image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    background_video_url = models.CharField(_('Background Video URL'), max_length=255, blank=True, null=True)
    layout = models.CharField(_('layout'), max_length=60, default='', blank=True)
    attributes = AttributesField()

    def __str__(self):
        return self.title or str(self.pk)

    def get_id(self):
        return slugify(self.title or 'section %s' % self.pk)


@python_2_unicode_compatible
class ShowcaseSlideshow(CMSPlugin):
    title = models.CharField(_('Anchor title'), max_length=255, blank=True, null=True)
    layout = models.CharField(_('layout'), max_length=60, default='', blank=True)
    attributes = AttributesField()

    def __str__(self):
        return self.title or str(self.pk)

    def get_id(self):
        return slugify(self.title or 'slideshow %s' % self.pk)


@python_2_unicode_compatible
class ShowcaseSlide(CMSPlugin):
    percentage = models.CharField(_('Percentage appears'), max_length=255, blank=True, null=True)
    landscape_image = FilerImageField(verbose_name=_('Landscape Image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    portrait_image = FilerImageField(verbose_name=_('Portrait Image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
    fade_in = models.BooleanField(_('Fade In'), default=False)
    fade_out = models.BooleanField(_('Fade Out'), default=False)
    layout = models.CharField(_('layout'), max_length=60, default='', blank=True)
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_id(self):
        return slugify('slide %s' % self.pk)


BooleanFieldPartial = partial(
    models.BooleanField,
    default=False,
)

for size in DEVICE_SIZES:
    ShowcaseSlideshow.add_to_class(
        '{}_hide'.format(size),
        BooleanFieldPartial(),
    )
    ShowcaseSection.add_to_class(
        '{}_hide'.format(size),
        BooleanFieldPartial(),
    )
