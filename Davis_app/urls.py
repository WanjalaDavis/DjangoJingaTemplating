from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('about/', views.AboutPage, name='about'),
    path('contact/', views.ContactPage, name='contact'),

]