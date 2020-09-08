from aldryn_client import forms

class Form(forms.BaseForm):
    section_layouts = forms.CharField(
        'Section layouts', required=False
    )
    slideshow_layouts = forms.CharField(
        'Slideshow layouts', required=False
    )
    slide_layouts = forms.CharField(
        'Slide layouts', required=False
    )
    hide_article = forms.CheckboxField(
        'Hide Showcase Article', required=False, initial=False
    )
    hide_slide = forms.CheckboxField(
        'Hide Showcase Slide', required=False, initial=False
    )

    def to_settings(self, data, settings):
        if data['section_layouts']:
            settings['SHOWCASE_SECTION_LAYOUTS'] = tuple(l.strip() for l in data['section_layouts'].split(','))
        if data['slideshow_layouts']:
            settings['SHOWCASE_SLIDESHOW_LAYOUTS'] = tuple(l.strip() for l in data['slideshow_layouts'].split(','))
        if data['slide_layouts']:
            settings['SHOWCASE_SLIDE_LAYOUTS'] = tuple(l.strip() for l in data['slide_layouts'].split(','))
        if data['hide_article']:
            settings['SHOWCASE_HIDE_ARTICLE'] = int(data['hide_article'])
        if data['hide_slide']:
            settings['SHOWCASE_HIDE_SLIDE'] = int(data['hide_slide'])
        return settings
