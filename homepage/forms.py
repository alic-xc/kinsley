from django import forms
from django.forms.widgets import TextInput

from homepage.models import Question


class UploadForm(forms.Form):
    img = forms.ImageField(allow_empty_file=False, required=True)


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control',
                                                                      'type': 'text', 'id': 'username',
                                                                      'placeholder': 'Enter Username'}))
    password = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control',
                                                                      'type': 'password', 'id': 'password',
                                                                      'placeholder': 'Enter Password'}))


class QuestionForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField(required=True)
    cough = forms.BooleanField(required=False)
    fever = forms.BooleanField(required=False)
    shaking_chills = forms.BooleanField(required=False)
    fast_heartbeat = forms.BooleanField(required=False)
    nausea = forms.BooleanField(required=False)
    vomiting = forms.BooleanField(required=False)
    muscle_pain = forms.BooleanField(required=False)
    cyanosis = forms.BooleanField(required=False)
    headache = forms.BooleanField(required=False)
