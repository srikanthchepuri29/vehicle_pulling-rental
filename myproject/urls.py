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
from myapp.views import home,Reports,Contact_us,login_view,register,logout_view,About,ride_page,book_ride,add_ride,passenger_settings_view, your_trips
from myapp.views import car, detail, booking, my_bookings, user_carpools_view, passenger_settings_view
from myapp.views import (
    portal_login_view, portal_logout_view, portal_rental_view, portal_rider_view, portal_carpool_view,
    portal_rental_bookings_view, portal_rental_cars_view, portal_rental_remaining_view, portal_rental_completed_view,
    portal_carpool_publish_view, portal_carpool_itineraries_view, portal_carpool_bookings_view,
    portal_rider_active_view, portal_rider_earnings_view, portal_rider_trips_view,
    api_request_ride, api_check_ride_status, api_accept_ride, api_update_ride_status, api_book_carpool_seat,
    get_carpool_offers, api_cancel_ride, api_submit_feedback
)
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('user/carpools/', user_carpools_view, name='user_carpools'),
    path('login/', login_view, name='login'),
    path('login/<str:portal_type>/', portal_login_view, name='portal_login'),
    path('portal/logout/', portal_logout_view, name='portal_logout'),
    path('portal/rental/', portal_rental_view, name='portal_rental'),
    path('portal/rental/bookings/', portal_rental_bookings_view, name='portal_rental_bookings'),
    path('portal/rental/cars/', portal_rental_cars_view, name='portal_rental_cars'),
    path('portal/rental/remaining/', portal_rental_remaining_view, name='portal_rental_remaining'),
    path('portal/rental/completed/', portal_rental_completed_view, name='portal_rental_completed'),
    path('portal/rider/', portal_rider_view, name='portal_rider'),
    path('portal/rider/active/', portal_rider_active_view, name='portal_rider_active'),
    path('portal/rider/earnings/', portal_rider_earnings_view, name='portal_rider_earnings'),
    path('portal/rider/trips/', portal_rider_trips_view, name='portal_rider_trips'),
    path('portal/carpool/', portal_carpool_view, name='portal_carpool'),
    path('portal/carpool/publish/', portal_carpool_publish_view, name='portal_carpool_publish'),
    path('portal/carpool/itineraries/', portal_carpool_itineraries_view, name='portal_carpool_itineraries'),
    path('portal/carpool/bookings/', portal_carpool_bookings_view, name='portal_carpool_bookings'),

    # Real-Time AJAX API endpoints
    path('api/ride/request/', api_request_ride, name='api_request_ride'),
    path('api/ride/status/<int:ride_id>/', api_check_ride_status, name='api_check_ride_status'),
    path('api/ride/accept/<int:ride_id>/', api_accept_ride, name='api_accept_ride'),
    path('api/ride/update/<int:ride_id>/', api_update_ride_status, name='api_update_ride_status'),
    path('api/ride/cancel/<int:ride_id>/', api_cancel_ride, name='api_cancel_ride'),
    path('api/ride/feedback/<int:ride_id>/', api_submit_feedback, name='api_submit_feedback'),
    path('api/carpool/book/<int:carpool_id>/', api_book_carpool_seat, name='api_book_carpool_seat'),
    path('api/carpool/list/', get_carpool_offers, name='get_carpool_offers'),

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
    path('your-trips/', your_trips, name='your_trips'),
    path('settings/', passenger_settings_view, name='passenger_settings'),

    path('register/',register,name='register'),
    path('logout/',logout_view,name='logout'),
    path('', include('myapp.urls')),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



