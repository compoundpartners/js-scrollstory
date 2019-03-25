# -*- coding: utf-8 -*-

from django.conf import settings

IMAGE_SECTION_LAYOUTS = getattr(
    settings,
    'SCROLLSTORY_IMAGE_SECTION_LAYOUTS',
    (),
)
COLUMN_LAYOUTS = getattr(
    settings,
    'SCROLLSTORY_COLUMN_LAYOUTS',
    (),
)
