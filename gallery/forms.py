from django import forms
from .models import Image,Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

            
class ImageForm(forms.ModelForm):
      class Meta:
            model = Image
            exclude = ['profile']
            image = forms.ImageField()
            name = forms.CharField(max_length=40)
            caption = forms.CharField()
            comments = forms.CharField()
            likes = forms.IntegerField()

