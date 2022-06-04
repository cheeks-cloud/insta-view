from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gallery.urls')), 
    path('accounts/', include('django_registration.backends.one_step.urls')),
]
