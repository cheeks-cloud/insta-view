from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('',views.welcome,name ='welcome'),
    path('photos/',views.photos,name = 'photos'),
    path('likes/',views.likes,name = 'likes'),
    path('comments/',views.comments,name = 'comments'),
    path('add/',views.new_photo,name = 'new-image'),
    path('login/',views.login_request,name = 'login'),
    path('search/',views.search_results,name = 'search'),
    path('register/',views.register_request,name = 'register'),
    path('logout/', views.logout_request, name= 'logout'),
    path('see/', views.see,name='see')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)