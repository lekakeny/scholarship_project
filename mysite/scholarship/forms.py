from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


def validate_username(value):
    User = get_user_model()
    user_exists = User.objects.filter(username=value).first()
    if user_exists:
        raise ValidationError(
            _('%(value)s exists'),
            params={'value': value},
        )


# bio-data
class BioDataForm(forms.Form):
    # registration details
    your_username = forms.CharField(label='Your username', max_length=100, validators=(validate_username,))
    your_firstname = forms.CharField(label='Your firstname', max_length=100)
    your_lastname = forms.CharField(label='Your lastname', max_length=100)
    password = forms.CharField(label='Your password', max_length=100, widget=forms.PasswordInput)
    # biodata
    your_address = forms.CharField(label='Your Address', max_length=100)
    your_mobile = forms.CharField(label='Your Mobile Number', max_length=100)
    your_email = forms.CharField(label='Your Email Address', max_length=100, widget=forms.EmailInput)
    your_birth = forms.FileField(label='Your Birth Certificate')
    your_naid = forms.FileField(label='Your National ID')


class SchoolForm(forms.Form):
    school_name = forms.CharField(label='Name of your School', max_length=100)
    school_address = forms.CharField(label='Your School Address', max_length=100)
    academic_level = forms.CharField(label='Your Academic Level', max_length=100)
    completion_year = forms.DateTimeField(label='Your Expected Year of Completion')


class ReasonForm(forms.Form):
    sponsorship_reasons = forms.CharField(label='In at most 500 words, write an essay on why you need this '
                                                'sponsorship', max_length=1000, widget=forms.Textarea)
    recommendation_letter = forms.FileField(label='Upload your letter of recommendation')
