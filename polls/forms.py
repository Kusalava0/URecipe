from email.mime import image
from django import forms


class UserImageForm(forms.Form):
    image = forms.ImageField(required=False)
