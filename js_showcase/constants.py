# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

SECTION_LAYOUTS = getattr(
    settings,
    'SHOWCASE_SECTION_LAYOUTS',
    (),
)
SLIDESHOW_LAYOUTS = getattr(
    settings,
    'SHOWCASE_SLIDESHOW_LAYOUTS',
    (),
)
SLIDE_LAYOUTS = getattr(
    settings,
    'SHOWCASE_SLIDE_LAYOUTS',
    (),
)
ADDITIONAL_CHILD_CLASSES = getattr(
    settings,
    'SHOWCASE_ADDITIONAL_CHILD_CLASSES',
    {},
)
ADDITIONAL_PARENT_CLASSES = getattr(
    settings,
    'SHOWCASE_ADDITIONAL_PARENT_CLASSES',
    {},
)
HIDE_ARTICLE = getattr(
    settings,
    'SHOWCASE_HIDE_ARTICLE',
    False,
)
HIDE_SLIDE = getattr(
    settings,
    'SHOWCASE_HIDE_SLIDE',
    False,
)
DEVICE_CHOICES = (
    ('xs', _('Extra small')),   # default <576px
    ('sm', _('Small')),         # default ≥576px
    ('md', _('Medium')),        # default ≥768px
    ('lg', _('Large')),         # default ≥992px
    ('xl', _('Extra large')),   # default ≥1200px
)
DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])
