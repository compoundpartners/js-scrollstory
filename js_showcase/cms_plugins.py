# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from . import models
from . import forms
from .constants import ADDITIONAL_CHILD_CLASSES, ADDITIONAL_PARENT_CLASSES


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
class ShowcaseContainerPlugin(CMSPluginBase):
    module = 'JumpSuite Showcase'
    model = models.ShowcaseContainer
    name = _('Showcase Container')
    admin_preview = False
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
            #'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context


@plugin_pool.register_plugin
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
            #'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context


@plugin_pool.register_plugin
class ShowcaseSectionPlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_showcase/section_%s.html'
    module = 'JumpSuite Showcase'
    model = models.ShowcaseSection
    form = forms.ShowcaseSectionForm
    name = _('Showcase Section')
    admin_preview = False
    render_template = 'js_showcase/section.html'
    allow_children = True
    parent_classes = ['ShowcaseArticlePlugin'] + ADDITIONAL_PARENT_CLASSES.get('ShowcaseSectionPlugin', [])
    exclude = ['attributes']

    def render(self, context, instance, placeholder):
        attributes = instance.attributes
        attributes['id'] = instance.get_id()
        attributes['class'] = 'story' + ' story-%s' % (instance.layout if instance.layout else 'center')
        if instance.background_color or instance.background_image:
            color_str = ' %s' % instance.background_color if instance.background_color else ''
            img_str = ' url(%s)' % instance.background_image.url if instance.background_image else ''
            attributes['style'] = 'background:%s%s;' % (color_str, img_str)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            #'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context


@plugin_pool.register_plugin
class ShowcaseSlideshowPlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_showcase/slideshow_%s.html'
    module = 'JumpSuite Showcase'
    model = models.ShowcaseSlideshow
    form = forms.ShowcaseSlideshowForm
    name = _('Showcase Slideshow')
    admin_preview = False
    render_template = 'js_showcase/slideshow.html'
    allow_children = True
    child_classes = ['ShowcaseSlidePlugin'] + ADDITIONAL_CHILD_CLASSES.get('ShowcaseSlideshowPlugin', [])
    #parent_classes = ['ShowcaseSectionPlugin']
    exclude = ['attributes']

    def render(self, context, instance, placeholder):
        attributes = {}
        attributes['id'] = instance.get_id()
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            #'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context


@plugin_pool.register_plugin
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
        attributes = {}
        attributes['id'] = instance.get_id()
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            #'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context

    # def get_layout(self, context, instance, placeholder):
        # if instance.parent:
            # plugin, _ = instance.parent.get_plugin_instance()
            # if hasattr(plugin, 'layout'):
              # return plugin.layout
        # return ''
