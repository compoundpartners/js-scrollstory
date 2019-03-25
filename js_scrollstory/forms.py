# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from . import models
from .constants import (
    IMAGE_SECTION_LAYOUTS,
    COLUMN_LAYOUTS,
)

IMAGE_SECTION_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + IMAGE_SECTION_LAYOUTS)), ('default',) + IMAGE_SECTION_LAYOUTS)
COLUMN_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('', 'left', 'right') + COLUMN_LAYOUTS)), ('center', 'left', 'right') + COLUMN_LAYOUTS)


class ScrollStoryImageSectionForm(forms.ModelForm):

    layout = forms.ChoiceField(IMAGE_SECTION_LAYOUTS_CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super(ScrollStoryImageSectionForm, self).__init__(*args, **kwargs)
        if len(IMAGE_SECTION_LAYOUTS) == 0:
            self.fields['layout'].widget = forms.HiddenInput()

    class Meta:
        model = models.ScrollStoryImageSection
        fields = ['title', 'background_image', 'content', 'layout']


class ScrollStoryColumnForm(forms.ModelForm):

    layout = forms.ChoiceField(COLUMN_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ScrollStoryColumn
        fields = ['title', 'background_image', 'background_color', 'layout']
