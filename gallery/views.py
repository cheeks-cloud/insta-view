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



def login(request):
  return render( request, "django_registration/login.html")


@login_required(login_url='/accounts/login/')
def new_photo(request):
  current_user = request.user
  if request.method == 'POST':
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
      image = form.save(commit=False)
      image.save()
    return redirect('profile.html')

  else:
    form = ImageForm()
  return render(request, 'new_image.html',{"form": form})