# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from . import models
from .constants import (
    SECTION_LAYOUTS,
    SLIDESHOW_LAYOUTS,
)

SECTION_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('', 'left', 'right') + SECTION_LAYOUTS)), ('center', 'left', 'right') + SECTION_LAYOUTS)

SLIDESHOW_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + SLIDESHOW_LAYOUTS)), ('default',) + SLIDESHOW_LAYOUTS)

class ShowcaseSectionForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=SECTION_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ShowcaseSection
        fields = '__all__'


class ShowcaseSlideshowForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=SLIDESHOW_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ShowcaseSlideshow
        fields = '__all__'
