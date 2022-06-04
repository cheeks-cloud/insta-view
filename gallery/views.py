from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
 
  return render( request, "index.html")

def photos(request):
  images = Image.objects.all()
  return render( request, "photos.html", {'images': images})
