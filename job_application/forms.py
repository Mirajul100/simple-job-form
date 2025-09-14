from django import forms

class ApplicationForm(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    phone = forms.CharField(max_length=80)
    position = forms.CharField(max_length=80)
    experience = forms.CharField(max_length=50)
    available = forms.DateField()
    terms = forms.BooleanField(required=False)
    newsletter = forms.BooleanField(required=False)