from django.urls import path
from . import views

urlpatterns = [
    path('add-ride/', views.add_ride, name='add_ride'),
    path('ride_page', views.ride_page, name='ride_page'),
    path('book-ride/', views.book_ride, name='book_ride'),


]