from django.urls import path
from django.conf import settings   
from django.conf.urls.static import static
from polls import views

urlpatterns = [
    
    path("home/", views.home),
    path("add/", views.add_recipes),
    path("edit/<id>", views.edit, name='Edit'),
    path("description/<recipe_title>", views.description, name='description'),
    path("My_recipes", views.my_recipe, name='myrecipe'),
    path("login/", views.user_login),
    path("logout/", views.user_logout),
    path("register/", views.register),
    path('', views.home),
    path('<nme>', views.rndm),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
