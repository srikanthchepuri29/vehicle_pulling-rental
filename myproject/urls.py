"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home
from myapp.views import home,Reports,Contact_us,login_view,register,logout_view,feature,About,ride_page,book_ride,add_ride
from myapp.views import car, detail, booking, my_bookings
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('feature/',feature,name="feature"),
    path('login/', login_view, name='login'),
    path('Reports/',Reports,name="Reports"),
    path('About/', About, name='About'),
    path('Contact_us/', Contact_us,name='Contact_us'),
    path('add-ride/', add_ride, name='add_ride'),
    path('ride_page/', ride_page, name='ride_page'),
    path('book-ride/', book_ride, name='book_ride'),
    path('car/', car, name='car'),
    path('detail/', detail, name='detail'),
    path('booking/', booking, name='booking'),
    path('my-bookings/', my_bookings, name='my_bookings'),

    path('register/',register,name='register'),
    path('logout/',logout_view,name='logout'),
    path('', include('myapp.urls')),

    
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



