# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from . import models
from . import forms
from .constants import (
    ADDITIONAL_CHILD_CLASSES,
    ADDITIONAL_PARENT_CLASSES,
    HIDE_ARTICLE,
    HIDE_SLIDE,
    DEVICE_SIZES,
)


class LayoutMixin():

    def get_layout(self, context, instance, placeholder):
        return instance.layout

    def get_render_template(self, context, instance, placeholder):
        layout = self.get_layout(context, instance, placeholder)
        if layout:
            template = self.TEMPLATE_NAME % layout
            try:
                select_template([template])
                return template
            except TemplateDoesNotExist:
                pass
        return self.render_template


@plugin_pool.register_plugin
class ShowcaseContainerPlugin(LayoutMixin, CMSPluginBase):
    module = 'JumpSuite Showcase'
    model = models.ShowcaseContainer
    form = forms.ShowcaseContainerForm
    name = _('Showcase Container')
    admin_preview = False
    TEMPLATE_NAME = 'js_showcase/container_%s.html'
    render_template = 'js_showcase/container.html'
    allow_children = True
    child_classes = ['ShowcaseArticlePlugin'] + ADDITIONAL_CHILD_CLASSES.get('ShowcaseContainerPlugin', [])
    exclude = ['attributes']

    def render(self, context, instance, placeholder):
        attributes = instance.attributes
        attributes['id'] = instance.get_id()
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class ShowcaseArticlePlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_showcase/article_%s.html'
    module = 'JumpSuite Showcase'
    model = models.ShowcaseArticle
    name = _('Showcase Article')
    admin_preview = False
    render_template = 'js_showcase/article.html'
    allow_children = True
    parent_classes = ['ShowcaseContainerPlugin'] + ADDITIONAL_PARENT_CLASSES.get('ShowcaseArticlePlugin', [])
    child_classes = ['ShowcaseSectionPlugin'] + ADDITIONAL_CHILD_CLASSES.get('ShowcaseArticlePlugin', [])
    exclude = ['attributes', 'layout']

    def render(self, context, instance, placeholder):
        attributes = instance.attributes
        attributes['id'] = instance.get_id()
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

if not HIDE_ARTICLE:
    plugin_pool.register_plugin(ShowcaseArticlePlugin)


@plugin_pool.register_plugin
class ShowcaseSectionPlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_showcase/section_%s.html'
    module = 'JumpSuite Showcase'
    model = models.ShowcaseSection
    form = forms.ShowcaseSectionForm
    name = _('Showcase Section')
    admin_preview = False
    render_template = 'js_showcase/section.html'
    change_form_template = 'js_showcase/admin/section.html'
    allow_children = True
    parent_classes = ['ShowcaseArticlePlugin'] + ADDITIONAL_PARENT_CLASSES.get('ShowcaseSectionPlugin', [])

    fieldsets = [
        (None, {
            'fields': (
                'title',
                'layout',
                'background_color',
                'background_image',
                'background_video_url',
            )
        }),
        (_('Responsive settings'), {
            'classes': ('collapse',),
            'fields': (
                ['{}_hide'.format(size) for size in DEVICE_SIZES],
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': ['attributes']
        }),
    ]

    def render(self, context, instance, placeholder):
        attributes = instance.attributes
        classes = []
        for device in DEVICE_SIZES:
            hide = getattr(instance, '{}_hide'.format(device))
            value = 'none' if hide else 'block'
            if device == 'xs':
                classes.append('d-%s' % value)
                prev = hide
            else:
                if hide != prev:
                    classes.append('d-%s-%s' % (device, value))
                    prev = hide
        classes.append('story' + ' story-%s' % (instance.layout if instance.layout else 'center'))
        attributes['class'] = ' '.join(classes)
        attributes['id'] = instance.get_id()
        if instance.background_color or instance.background_image:
            color_str = ' %s' % instance.background_color if instance.background_color else ''
            img_str = ' url(%s)' % instance.background_image.url if instance.background_image else ''
            attributes['style'] = 'background:%s%s;' % (color_str, img_str)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class ShowcaseSlideshowPlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_showcase/slideshow_%s.html'
    module = 'JumpSuite Showcase'
    model = models.ShowcaseSlideshow
    form = forms.ShowcaseSlideshowForm
    name = _('Showcase Slideshow')
    admin_preview = False
    render_template = 'js_showcase/slideshow.html'
    change_form_template = 'js_showcase/admin/slideshow.html'
    allow_children = True
    child_classes = ['ShowcaseSlidePlugin'] + ADDITIONAL_CHILD_CLASSES.get('ShowcaseSlideshowPlugin', [])
    #parent_classes = ['ShowcaseSectionPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'title',
                'layout',
            )
        }),
        (_('Responsive settings'), {
            'classes': ('collapse',),
            'fields': (
                ['{}_hide'.format(size) for size in DEVICE_SIZES],
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': ['attributes']
        }),
    ]
    def render(self, context, instance, placeholder):
        classes = []
        for device in DEVICE_SIZES:
            hide = getattr(instance, '{}_hide'.format(device))
            value = 'none' if hide else 'block'
            if device == 'xs':
                classes.append('d-%s' % value)
                prev = hide
            else:
                if hide != prev:
                    classes.append('d-%s-%s' % (device, value))
                    prev = hide
        instance.attributes['class'] = ' '.join(classes)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class ShowcaseSlidePlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_showcase/slide_%s.html'
    module = 'JumpSuite Showcase'
    model = models.ShowcaseSlide
    form = forms.ShowcaseSlideForm
    name = _('Showcase Slide')
    admin_preview = False
    render_template = 'js_showcase/slide.html'
    allow_children = True
    #parent_classes = ['ShowcaseSlideShowPlugin'] + ADDITIONAL_PARENT_CLASSES.get('ShowcaseSlidePlugin', [])
    exclude = ['attributes']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

if not HIDE_SLIDE:
    plugin_pool.register_plugin(ShowcaseSlideshowPlugin)
    plugin_pool.register_plugin(ShowcaseSlidePlugin)
