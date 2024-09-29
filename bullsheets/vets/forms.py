from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, HTML, ButtonHolder, Submit

from .models import Vet

class VetForm(forms.ModelForm):
    class Meta:
        model = Vet
        fields = ('fname', 'lname', 'title', 'practice_name', 'email', 'phone', 'address1', 'address2', 'city', 'state', 'zip', 'website', 'license')

    def __init__(self, *args, **kwargs):
        super(VetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-vetForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_vet'
        self.helper.layout = Layout(
            Fieldset(
                'Vet Information',
                Field('fname', placeholder='First Name'),
                Field('lname', placeholder='Last Name'),
                Field('title', placeholder='Title'),
                Field('practice_name', placeholder='Practice Name'),
                Field('email', placeholder='Email'),
                Field('phone', placeholder='Phone'),
                Field('address1', placeholder='Address 1'),
                Field('address2', placeholder='Address 2'),
                Field('city', placeholder='City'),
                Field('state', placeholder='State'),
                Field('zip', placeholder='Zip'),
                Field('website', placeholder='Website'),
                Field('license', placeholder='License'),

            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-primary')
            )
        )