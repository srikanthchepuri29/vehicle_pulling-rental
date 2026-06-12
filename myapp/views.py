from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Ride, CarpoolRide, CarBooking
from datetime import datetime

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

def home(request):
    return render(request,'home.html')


def feature(request):
    return render(request,'features.html')

def Reports(request):
    post=Contact.objects.all()
    return render(request,"index.html",{'post':post})




def Contact_us(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject = request.POST.get('subject')
        message=request.POST.get('message')
        image=request.FILES.get('image')
        
        k=Contact(name=name,email=email,subject=subject,message=message,image=image)
        k.save()
    return render(request,"Contact.html")




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def create_blog(request):
    return render(request,'create_blog.html')

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def About(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Feedback')   # reload page after submit
    else:
        form = FeedbackForm()

    return render(request, 'About.html', {'form': form})


from django.shortcuts import render, redirect



#  Main Page
def ride_page(request):
    return render(request, 'ride_map.html')


#  Book Bike Ride
def book_ride(request):
    if request.method == "POST":
        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')
        distance = request.POST.get('distance')

        if distance:
            distance = float(distance)
            price = distance * 10   # 💰 price calculation

            Ride.objects.create(
                pickup=pickup,
                drop=drop,
                distance=distance,
                price=price
            )

    return redirect('ride_page')


#  Add Carpool Ride (BlaBlaCar)
def add_ride(request):
    if request.method == "POST":
        CarpoolRide.objects.create(
            start_location=request.POST.get('start'),
            destination=request.POST.get('destination'),
            date=request.POST.get('date'),
            time=request.POST.get('time'),
            seats=request.POST.get('seats')
        )

    return redirect('ride_page')

def car(request):
    return render(request, 'car.html')


def detail(request):
    car_name = request.GET.get('name', 'Mercedes Benz S-Class')
    car_price = request.GET.get('price', '15000')
    car_image = request.GET.get('image', 'car-rent-1.png')
    car_year = request.GET.get('year', '2023')
    car_trans = request.GET.get('trans', 'AUTO')
    car_mileage = request.GET.get('mileage', '5K')
    
    context = {
        'car_name': car_name,
        'car_price': car_price,
        'car_image': car_image,
        'car_year': car_year,
        'car_trans': car_trans,
        'car_mileage': car_mileage,
    }
    return render(request, 'detail.html', context)


def booking(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        pickup_location = request.POST.get('pickup_location')
        drop_location = request.POST.get('drop_location')
        pickup_date_str = request.POST.get('pickup_date')
        drop_date_str = request.POST.get('drop_date')
        pickup_time_str = request.POST.get('pickup_time')
        adults = int(request.POST.get('adults', 1))
        children = int(request.POST.get('children', 0))
        special_request = request.POST.get('special_request', '')
        car_name = request.POST.get('car_name', 'Mercedes Benz S-Class')
        car_price = float(request.POST.get('car_price', 15000.0))
        car_image = request.POST.get('car_image', 'car-rent-1.png')
        
        addon_child_seat = request.POST.get('addon_child_seat') == 'on'
        addon_additional_driver = request.POST.get('addon_additional_driver') == 'on'
        addon_premium_insurance = request.POST.get('addon_premium_insurance') == 'on'
        
        payment_method = request.POST.get('payment', 'banktransfer')
        card_number = request.POST.get('card_number', '')
        card_expiry = request.POST.get('card_expiry', '')
        card_cvv = request.POST.get('card_cvv', '')
        
        # Date & Price Calculations
        days = 1
        if pickup_date_str and drop_date_str:
            try:
                p_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
                d_date = datetime.strptime(drop_date_str, '%Y-%m-%d').date()
                diff = (d_date - p_date).days
                if diff > 0:
                    days = diff
            except ValueError:
                pass
        
        # Rates
        addon_total = 0.0
        if addon_child_seat:
            addon_total += 1500.0
        if addon_additional_driver:
            addon_total += 2500.0
        if addon_premium_insurance:
            addon_total += 5000.0
            
        daily_total = car_price + addon_total
        final_total = days * daily_total
        
        # Parse Pickup Date
        parsed_pickup_date = datetime.now().date()
        if pickup_date_str:
            try:
                parsed_pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass
        
        # Save Booking
        booking_obj = CarBooking.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            pickup_location=pickup_location,
            drop_location=drop_location,
            pickup_date=parsed_pickup_date,
            pickup_time=pickup_time_str if pickup_time_str else "10:00",
            adults=adults,
            children=children,
            special_request=special_request,
            car_name=car_name,
            car_price=car_price,
            car_image=car_image,
            addon_child_seat=addon_child_seat,
            addon_additional_driver=addon_additional_driver,
            addon_premium_insurance=addon_premium_insurance,
            payment_method=payment_method,
            card_number=card_number,
            card_expiry=card_expiry,
            card_cvv=card_cvv,
            total_price=final_total
        )
        
        messages.success(request, f"Successfully booked {car_name}! Your booking reference is RS-{booking_obj.id}.")
        return redirect('my_bookings')
        
    # GET request
    car_name = request.GET.get('name', 'Mercedes Benz S-Class')
    car_price = request.GET.get('price', '15000')
    car_image = request.GET.get('image', 'car-rent-1.png')
    
    context = {
        'car_name': car_name,
        'car_price': car_price,
        'car_image': car_image,
    }
    return render(request, 'booking.html', context)


def my_bookings(request):
    bookings = CarBooking.objects.all().order_by('-created_at')
    return render(request, 'my_bookings.html', {'bookings': bookings})