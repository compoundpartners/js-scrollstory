# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from . import models
from . import forms


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
class ScrollStoryContainerPlugin(CMSPluginBase):
    module = 'JumpSuite ScrollStory'
    model = models.ScrollStoryContainer
    name = _('ScrollStory Container')
    admin_preview = False
    render_template = 'js_scrollstory/container.html'
    allow_children = True
    child_classes = ['ScrollStoryImageSectionPlugin', 'ScrollStoryColumnPlugin']

    def render(self, context, instance, placeholder):
        attributes = {}
        attributes['id'] = instance.get_id()
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context


@plugin_pool.register_plugin
class ScrollStoryImageSectionPlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_scrollstory/image_%s.html'
    module = 'JumpSuite ScrollStory'
    model = models.ScrollStoryImageSection
    form = forms.ScrollStoryImageSectionForm
    name = _('ScrollStory Image Section')
    admin_preview = False
    render_template = 'js_scrollstory/image.html'
    parent_classes = ['ScrollStoryContainerPlugin']

    def render(self, context, instance, placeholder):
        attributes = {}
        attributes['id'] = instance.get_id()
        attributes['class'] = 'story story-image'# + (' story-image-%s' % instance.layout) if instance.layout else ''
        attributes['style'] = 'background:url(%s);' %  instance.background_image.url
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context


@plugin_pool.register_plugin
class ScrollStoryColumnPlugin(LayoutMixin, CMSPluginBase):
    TEMPLATE_NAME = 'js_scrollstory/column_%s.html'
    module = 'JumpSuite ScrollStory'
    model = models.ScrollStoryColumn
    form = forms.ScrollStoryColumnForm
    name = _('ScrollStory Column')
    admin_preview = False
    render_template = 'js_scrollstory/column.html'
    allow_children = True
    parent_classes = ['ScrollStoryContainerPlugin']

    def render(self, context, instance, placeholder):
        attributes = {}
        attributes['id'] = instance.get_id()
        attributes['class'] = 'story' + ' story-%s' % (instance.layout if instance.layout else 'center')
        if instance.background_color or instance.background_image:
            color_str = ' %s' % instance.background_color if instance.background_color else ''
            img_str = ' url(%s)' % instance.background_image.url if instance.background_image else ''
            attributes['style'] = 'background:%s%s;' % (color_str, img_str)
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'attributes_str': mark_safe(' '.join(['%s="%s"' % a for a in attributes.items()]))
        })
        return context
