from django.shortcuts import render,redirect
from .models import Image,Profile

# Create your views here.
def welcome(request):
 
  return render( request, "index.html")

def photos(request):
  images = Image.objects.all()
  return render( request, "photos.html", {'images': images})
