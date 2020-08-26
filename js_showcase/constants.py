# -*- coding: utf-8 -*-

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
