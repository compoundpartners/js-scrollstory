from aldryn_client import forms

class Form(forms.BaseForm):
    section_layouts = forms.CharField(
        'Section layouts', required=False, initial=False
    )
    slideshow_layouts = forms.CharField(
        'Slideshow layouts', required=False, initial=False
    )

    def to_settings(self, data, settings):
        if data['section_layouts']:
            settings['SHOWCASE_SECTION_LAYOUTS'] = tuple(l.strip() for l in data['section_layouts'].split(','))
        if data['slideshow_layouts']:
            settings['SHOWCASE_SLIDESHOW_LAYOUTS'] = tuple(l.strip() for l in data['slideshow_layouts'].split(','))
        return settings
