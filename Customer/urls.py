from django.urls import path

from .import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('gallery',views.gallery,name='gallery'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
]