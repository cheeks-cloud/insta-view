from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.photos,name = 'photos'),
    path('add/',views.new_photo,name = 'new-image'),
    path('login/',views.login,name = 'login'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)