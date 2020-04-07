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
