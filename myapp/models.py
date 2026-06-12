from django.db import models
from django.db import models
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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.car_name}"

    
