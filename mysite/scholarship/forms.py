from django import forms
from . import models


class PersonalForm(forms.ModelForm):
    class Meta:
        model = models.Scholarship
        fields = "__all__"
