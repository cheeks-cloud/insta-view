from django.http import Http404
from django.shortcuts import render,redirect
from .models import Image,Profile,Comments,Likes
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def welcome(request):
 
  return render( request, "index.html")

def photos(request):
  images = Image.objects.all()
  return render( request, "photos.html", {'images': images})

def likes(request):
  likes = Likes.objects.all()
  return render( request, "likes.html", {'likes':likes})
def comments(request):

  comments = Comments.objects.all()

  return render( request, "comments.html", {'comments': comments})

def register_request(request):
  if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          messages.success(request, "Registration successful." )
        return redirect('/login/')
  messages.error(request, "Unsuccessful registration. Invalid information.")
  form = NewUserForm()
  return render (request=request, template_name="registration_form.html", context={"register_form":form})


def login_request(request):
  if request.method == "POST":
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
          username = form.cleaned_data.get('username')
          password = form.cleaned_data.get('password')
          user = authenticate(username=username, password=password)
          if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('/photos/')
          else:
            messages.error(request,"Invalid username or password.")
      else:
          messages.error(request,"Invalid username or password.")
  form = AuthenticationForm()
  return render(request=request, template_name="django_registration/login.html", context={"login_form":form})
  

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return render( request, "index.html")


@login_required(login_url='/login/')
def new_photo(request):
   current_user = request.user
   if request.method == 'POST':
     form = ImageForm(request.POST,request.FILES)
     if form.is_valid():
       image = form.save()
       image.profile = current_user
       image.save_image()
     return redirect('/photos/')

   else:
    form = ImageForm()
   return render(request, 'new_image.html',{"form": form})


def see(request):
    img = Image.objects.all().first()
    context={
      'imgs':img
    }
    
    return render( request, "profile.html",context)

def search_results(request):
   if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_images})

   else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})