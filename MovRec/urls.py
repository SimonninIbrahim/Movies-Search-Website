from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('start/' , views.start),
    path('sign/' , views.sign),
    path('search/' , views.search),
    path('profile/' , views.profile),
]