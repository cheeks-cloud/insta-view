from django import forms
from .models import Image,Profile

class ImageForm(forms.Form):
  image = forms.ImageField(null=False, blank=False, upload_to='images/')
  name = forms.CharField(max_length=40,null=False, blank=False)
  caption = forms.TextField(null=False, blank=False)
  comments = forms.TextField(null=False, blank=False)
  likes = forms.IntegerField(null=False, blank=False)

