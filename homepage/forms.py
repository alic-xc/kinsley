from django import forms
from .models import *


class Upload_form(forms.Form):
    img = forms.ImageField(allow_empty_file=False, required=True)