from aldryn_client import forms

class Form(forms.BaseForm):
    image_section_layouts = forms.CheckboxField(
        'Image Section layouts', required=False, initial=False
    )
    column_layouts = forms.CheckboxField(
        'Column layouts', required=False, initial=False
    )

    def to_settings(self, data, settings):
        if data['image_section_layouts']:
            settings['SCROLLSTORY_IMAGE_SECTION_LAYOUTS'] = tuple(l.strip() for l in data['image_section_layouts'].split(','))
        if data['column_layouts']:
            settings['SCROLLSTORY_COLUMN_LAYOUTS'] = tuple(l.strip() for l in data['column_layouts'].split(','))
        return settings
