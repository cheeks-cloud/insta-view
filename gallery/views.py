from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
# Create your views here.
# def welcome(request):
 
#   return render( request, "index.html")

def photos(request):
  images = Image.objects.all()
  return render( request, "photos.html", {'images': images})

def new_photo(request):
  if request.method == 'POST':
    if form.is_valid():
      image = form.save(commit=False)
      image.save()
    return redirect('')

  else:
    form = ImageForm()
  return render(request, 'profile.html',{"form": form})