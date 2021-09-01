from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login', views.login, name='login'),
    path('accounts/logout', views.logout, name='logout'),
    path('accounts/register', views.register, name='register'),
    path('gallery/', views.gallery, name='gallery'),
    path('admin/', views.admin_view, name='admin'),
    path('chairperson/', views.chairperson_view, name='chairperson'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),  # get photo by id
    path('add/', views.addPhoto, name='addphoto'),

]
