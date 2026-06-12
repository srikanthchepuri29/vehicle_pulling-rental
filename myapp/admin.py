from django.contrib import admin
from .models import Contact,Feedback
from .models import Ride, CarpoolRide


admin.site.register(Contact)
admin.site.register(Feedback)



@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('pickup', 'drop', 'distance', 'price', 'created_at')


@admin.register(CarpoolRide)
class CarpoolRideAdmin(admin.ModelAdmin):
    list_display = ('start_location', 'destination', 'date', 'time', 'seats')

