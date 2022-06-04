from django import forms
from .models import Image,Profile

class ImageForm(forms.ModelForm):
      class Meta:
            model = Image
            exclude = ['profile']
            image = forms.ImageField()
            name = forms.CharField(max_length=40)
            caption = forms.CharField()
            comments = forms.CharField()
            likes = forms.IntegerField()

