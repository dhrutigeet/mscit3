from django import forms
from .models import ExampleModel

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
	
class loginForm(forms.Form):
	username=forms.CharField(required=True)
	password=forms.CharField(max_length=32, widget=forms.PasswordInput)