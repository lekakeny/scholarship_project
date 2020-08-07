from django import forms
from . import models


class PersonalForm(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = "__all__"
