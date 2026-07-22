from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Ride(models.Model):
    pickup = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    distance = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pickup} → {self.drop}"


class CarpoolRide(models.Model):
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.start_location} → {self.destination}"

class CarBooking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    drop_date = models.DateField(null=True, blank=True)
    drop_time = models.TimeField(null=True, blank=True)
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    special_request = models.TextField(blank=True, null=True)
    car_name = models.CharField(max_length=150)
    car_price = models.FloatField()
    car_image = models.CharField(max_length=255)
    addon_child_seat = models.BooleanField(default=False)
    addon_additional_driver = models.BooleanField(default=False)
    addon_premium_insurance = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20, blank=True, null=True)
    card_expiry = models.CharField(max_length=10, blank=True, null=True)
    card_cvv = models.CharField(max_length=4, blank=True, null=True)
    total_price = models.FloatField(default=0.0)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.car_name}"


class TaxiRideRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taxi_bookings')
    pickup = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    distance = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    pin = models.CharField(max_length=4)
    driver_name = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Accepted', 'Accepted'),
            ('Arrived', 'Arrived'),
            ('In_Progress', 'In Progress'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    cancel_reason = models.TextField(blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"TaxiRS-{self.id} ({self.status}) for {self.user.username}"


class CarpoolOffer(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_carpools')
    vehicle_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)
    start_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()
    plans_free_booking = models.BooleanField(default=True)
    vehicle_type = models.CharField(max_length=20, default='car')
    price = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Upcoming', 'Upcoming'),
            ('In_Progress', 'In Progress'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ],
        default='Upcoming'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CarpoolOffer-{self.id}: {self.start_location} -> {self.destination}"


class CarpoolSeatBooking(models.Model):
    carpool = models.ForeignKey(CarpoolOffer, on_delete=models.CASCADE, related_name='seat_bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carpool_trips')
    seats_booked = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default='Pending')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.user.username} on Carpool {self.carpool.id}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    work_address = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    portal_role = models.CharField(max_length=20, default='user')

    def __str__(self):
        return f"{self.user.username}'s profile"

    @property
    def image(self):
        return self.profile_image

    @image.setter
    def image(self, value):
        self.profile_image = value

    @property
    def mobile_number(self):
        return self.phone

    @mobile_number.setter
    def mobile_number(self, value):
        self.phone = value
        
    @property
    def location(self):
        return self.home_address

    @location.setter
    def location(self, value):
        self.home_address = value

    

class RemovedCar(models.Model):
    REASON_CHOICES = [
        ('damaged', 'Damaged'),
        ('out_of_service', 'Out of Service'),
        ('sold', 'Sold / Decommissioned'),
        ('maintenance', 'Under Maintenance'),
        ('other', 'Other'),
    ]
    car_name = models.CharField(max_length=150, unique=True)
    reason = models.CharField(max_length=30, choices=REASON_CHOICES, default='out_of_service')
    removed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    removed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car_name} ({self.get_reason_display()})"

