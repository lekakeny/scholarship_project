from django import forms
from . import models


# bio-data
class BioDataForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
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
    recommendation_letter = forms.FileField(label='Upload your letter of recommendation', max_length=100)
