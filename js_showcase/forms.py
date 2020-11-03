# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.text import slugify
from djangocms_attributes_field.fields import AttributesFormField
from . import models
from .constants import (
    CONTAINER_LAYOUTS,
    SECTION_LAYOUTS,
    SLIDESHOW_LAYOUTS,
    SLIDE_LAYOUTS,
    DEVICE_SIZES,
)

CONTAINER_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + CONTAINER_LAYOUTS)), ('default',) + CONTAINER_LAYOUTS)

SECTION_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + SECTION_LAYOUTS)), ('default',) + SECTION_LAYOUTS)

SLIDESHOW_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + SLIDESHOW_LAYOUTS)), ('default',) + SLIDESHOW_LAYOUTS)

SLIDE_LAYOUTS_CHOICES = zip(list(map(lambda s: slugify(s).replace('-', '_'), ('',) + SLIDE_LAYOUTS)), ('default',) + SLIDE_LAYOUTS)


class ShowcaseContainerForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=CONTAINER_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ShowcaseContainer
        fields = '__all__'


class ShowcaseSectionBaseForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=SECTION_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ShowcaseSection
        fields = '__all__'


class ShowcaseSlideshowBaseForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=SLIDESHOW_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ShowcaseSlideshow
        fields = '__all__'


class ShowcaseSlideForm(forms.ModelForm):

    layout = forms.ChoiceField(choices=SLIDE_LAYOUTS_CHOICES, required=False)

    class Meta:
        model = models.ShowcaseSlide
        fields = '__all__'


extra_fields_column = {}
for size in DEVICE_SIZES:
    extra_fields_column['{}_hide'.format(size)] = forms.BooleanField(
        label='hide {}'.format(size),
        required=False,
    )

ShowcaseSlideshowForm = type(
    str('Bootstrap4GridColumnBaseForm'),
    (ShowcaseSlideshowBaseForm,),
    extra_fields_column,
)

ShowcaseSectionForm = type(
    str('Bootstrap4GridColumnBaseForm'),
    (ShowcaseSectionBaseForm,),
    extra_fields_column,
)
