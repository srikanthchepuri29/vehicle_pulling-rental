from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Contact
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Ride, CarpoolRide, CarBooking, TaxiRideRequest, CarpoolOffer, CarpoolSeatBooking, UserProfile, RemovedCar
from datetime import datetime
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q



SHOWROOM_CARS = [
    # --- Luxury Sedans (6) ---
    {
        'id': 1,
        'name': 'Mercedes Benz S-Class',
        'price': 15000.0,
        'image': 'car-rent-1.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '10 kmpl',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Petrol'
    },
    {
        'id': 2,
        'name': 'BMW 7 Series',
        'price': 14000.0,
        'image': 'car-rent-2.png',
        'year': '2022',
        'trans': 'AUTO',
        'mileage': '11 kmpl',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Diesel'
    },
    {
        'id': 3,
        'name': 'Audi A8',
        'price': 14500.0,
        'image': 'car-rent-3.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '10 kmpl',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Petrol'
    },
    {
        'id': 4,
        'name': 'Lexus LS 500',
        'price': 12000.0,
        'image': 'car-rent-4.png',
        'year': '2021',
        'trans': 'AUTO',
        'mileage': '12 kmpl',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Hybrid'
    },
    {
        'id': 5,
        'name': 'Jaguar XJ',
        'price': 11000.0,
        'image': 'car-rent-5.png',
        'year': '2020',
        'trans': 'AUTO',
        'mileage': '9 kmpl',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Petrol'
    },
    {
        'id': 6,
        'name': 'Porsche Panamera',
        'price': 16000.0,
        'image': 'car-rent-6.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '8 kmpl',
        'type': 'sedan',
        'seats': 4,
        'fuel': 'Petrol'
    },

    # --- Premium SUVs (6) ---
    {
        'id': 7,
        'name': 'Range Rover',
        'price': 18000.0,
        'image': 'car-rent-1.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '9 kmpl',
        'type': 'suv',
        'seats': 5,
        'fuel': 'Diesel'
    },
    {
        'id': 8,
        'name': 'BMW X7',
        'price': 17000.0,
        'image': 'car-rent-2.png',
        'year': '2022',
        'trans': 'AUTO',
        'mileage': '8 kmpl',
        'type': 'suv',
        'seats': 7,
        'fuel': 'Petrol'
    },
    {
        'id': 9,
        'name': 'Audi Q8',
        'price': 16500.0,
        'image': 'car-rent-3.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '10 kmpl',
        'type': 'suv',
        'seats': 5,
        'fuel': 'Petrol'
    },
    {
        'id': 10,
        'name': 'Mercedes GLS',
        'price': 17500.0,
        'image': 'car-rent-4.png',
        'year': '2022',
        'trans': 'AUTO',
        'mileage': '9 kmpl',
        'type': 'suv',
        'seats': 7,
        'fuel': 'Diesel'
    },
    {
        'id': 11,
        'name': 'Porsche Cayenne',
        'price': 19000.0,
        'image': 'car-rent-5.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '9 kmpl',
        'type': 'suv',
        'seats': 5,
        'fuel': 'Petrol'
    },
    {
        'id': 12,
        'name': 'Lexus LX 600',
        'price': 18500.0,
        'image': 'car-rent-6.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '7 kmpl',
        'type': 'suv',
        'seats': 7,
        'fuel': 'Petrol'
    },

    # --- Electric (6) ---
    {
        'id': 13,
        'name': 'Tesla Model S',
        'price': 15000.0,
        'image': 'car-rent-1.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '400 km range',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Electric'
    },
    {
        'id': 14,
        'name': 'Porsche Taycan',
        'price': 20000.0,
        'image': 'car-rent-2.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '350 km range',
        'type': 'sedan',
        'seats': 4,
        'fuel': 'Electric'
    },
    {
        'id': 15,
        'name': 'Audi e-tron GT',
        'price': 18000.0,
        'image': 'car-rent-3.png',
        'year': '2022',
        'trans': 'AUTO',
        'mileage': '380 km range',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Electric'
    },
    {
        'id': 16,
        'name': 'Mercedes EQS',
        'price': 19000.0,
        'image': 'car-rent-4.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '450 km range',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Electric'
    },
    {
        'id': 17,
        'name': 'Lucid Air',
        'price': 21000.0,
        'image': 'car-rent-5.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '500 km range',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Electric'
    },
    {
        'id': 18,
        'name': 'BMW i7',
        'price': 19500.0,
        'image': 'car-rent-6.png',
        'year': '2023',
        'trans': 'AUTO',
        'mileage': '420 km range',
        'type': 'sedan',
        'seats': 5,
        'fuel': 'Electric'
    }
]


def home(request):
    unrated_ride = None
    if request.user.is_authenticated:
        unrated_ride = TaxiRideRequest.objects.filter(
            user=request.user,
            status='Completed',
            rating__isnull=True
        ).order_by('-created_at').first()
        
    return render(request, 'home.html', {
        'unrated_ride': unrated_ride
    })





def Reports(request):
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    post=Contact.objects.all()
    return render(request,"index.html",{'post':post})





def Contact_us(request):
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
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
            profile, _ = UserProfile.objects.get_or_create(user=user)
            if profile.portal_role != 'user':
                return render(request, 'login.html', {
                    'error': f'Invalid credentials. This account is registered for the {profile.portal_role.upper()} portal.'
                })
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

        # Create user profile with 'user' role
        profile = UserProfile.objects.create(user=user, portal_role='user')
        profile.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def create_blog(request):
    return render(request,'create_blog.html')


def About(request):
    from .forms import FeedbackForm
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('About')   # reload page after submit
    else:
        form = FeedbackForm()

    return render(request, 'About.html', {'form': form})



def ride_page(request):
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    active_ride = TaxiRideRequest.objects.filter(
        user=request.user,
        status__in=['Pending', 'Accepted', 'Arrived', 'In_Progress']
    ).last()
    
    unrated_ride = TaxiRideRequest.objects.filter(
        user=request.user,
        status='Completed',
        rating__isnull=True
    ).order_by('-created_at').first()
    
    return render(request, 'ride_map.html', {
        'active_ride': active_ride,
        'unrated_ride': unrated_ride
    })

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
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    return render(request, 'car.html')



def detail(request):
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    car_name = request.GET.get('name', 'Mercedes Benz S-Class')
    car_price = request.GET.get('price', '15000')
    if car_price:
        import re
        car_price = re.sub(r'[^\d.]', '', car_price)
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
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
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
        car_price_raw = request.POST.get('car_price', '15000.0')
        import re
        cleaned_price = re.sub(r'[^\d.]', '', str(car_price_raw))
        car_price = float(cleaned_price) if cleaned_price else 15000.0
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
        
        # Parse Pickup & Drop Dates
        parsed_pickup_date = datetime.now().date()
        if pickup_date_str:
            try:
                parsed_pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        parsed_drop_date = None
        if drop_date_str:
            try:
                parsed_drop_date = datetime.strptime(drop_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass
        
        drop_time_str = request.POST.get('drop_time')
        
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
            drop_date=parsed_drop_date,
            drop_time=drop_time_str if drop_time_str else "12:00",
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
    if car_price:
        import re
        car_price = re.sub(r'[^\d.]', '', car_price)
    car_image = request.GET.get('image', 'car-rent-1.png')
    
    context = {
        'car_name': car_name,
        'car_price': car_price,
        'car_image': car_image,
    }
    return render(request, 'booking.html', context)



def my_bookings(request):
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    bookings = CarBooking.objects.all().order_by('-created_at')
    return render(request, 'my_bookings.html', {'bookings': bookings})


# --- Portal authentication views ---


@login_required
def your_trips(request):
    trips = TaxiRideRequest.objects.filter(user=request.user).order_by('-created_at')
    
    # Precompute metrics
    total_bookings = trips.count()
    completed_bookings = trips.filter(status='Completed').count()
    cancelled_bookings = trips.filter(status='Cancelled').count()
    total_spent = sum(t.price for t in trips.filter(status='Completed'))
    
    for trip in trips:
        ratio = 10
        if trip.distance > 0:
            ratio = trip.price / trip.distance
            
        if ratio <= 6:
            trip.derived_vehicle_type = 'Bike'
            trip.derived_vehicle_icon = '🏍️'
            trip.derived_vehicle_details = 'Express Bike (Honda Unicorn)'
            trip.derived_vehicle_plate = f'TS 12 BK {1000 + (trip.id % 9000)}'
        elif ratio <= 12:
            trip.derived_vehicle_type = 'Auto'
            trip.derived_vehicle_icon = '🛺'
            trip.derived_vehicle_details = 'Auto Rickshaw (Bajaj RE)'
            trip.derived_vehicle_plate = f'TS 09 AT {2000 + (trip.id % 9000)}'
        else:
            trip.derived_vehicle_type = 'Cab'
            trip.derived_vehicle_icon = '🚗'
            trip.derived_vehicle_details = 'Premium Sedan (Suzuki Dzire)'
            trip.derived_vehicle_plate = f'TS 08 CB {3000 + (trip.id % 9000)}'
            
        if not trip.driver_name:
            if trip.status == 'Completed':
                trip.derived_driver_name = 'Rahul Sharma'
            elif trip.status == 'Cancelled':
                trip.derived_driver_name = 'Not Assigned'
            else:
                trip.derived_driver_name = 'Searching...'
        else:
            trip.derived_driver_name = trip.driver_name
            
    context = {
        'trips': trips,
        'total_bookings': total_bookings,
        'completed_bookings': completed_bookings,
        'cancelled_bookings': cancelled_bookings,
        'total_spent': total_spent,
    }
    return render(request, 'your_trips.html', context)


def portal_login_view(request, portal_type):
    # portal_type can be: 'user', 'rental', 'rider', 'carpool'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            profile, _ = UserProfile.objects.get_or_create(user=user)
            if profile.portal_role != portal_type:
                return render(request, 'portal_login.html', {
                    'portal_type': portal_type,
                    'error': f'Invalid credentials. This account is registered for the {profile.portal_role.upper()} portal, not {portal_type.upper()}.'
                })
            
            login(request, user)
            request.session['portal_role'] = portal_type
            if portal_type == 'rental':
                return redirect('portal_rental')
            elif portal_type == 'rider':
                return redirect('portal_rider')
            elif portal_type == 'carpool':
                return redirect('portal_carpool')
            else:
                return redirect('home')
        else:
            return render(request, 'portal_login.html', {
                'portal_type': portal_type,
                'error': 'Invalid credentials. Please register or check your login data.'
            })

    return render(request, 'portal_login.html', {'portal_type': portal_type})


def portal_register_view(request, portal_type):
    # portal_type can be: 'user', 'rental', 'rider', 'carpool'
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        phone = request.POST.get('phone', '').strip()
        location = request.POST.get('location', '').strip()
        extra_detail = request.POST.get('extra_detail', '').strip()

        if password != confirm_password:
            return render(request, 'portal_register.html', {
                'portal_type': portal_type,
                'error': 'Passwords do not match.',
                'form_data': request.POST
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'portal_register.html', {
                'portal_type': portal_type,
                'error': 'Username already exists.',
                'form_data': request.POST
            })

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        # Create user profile
        user_profile = UserProfile.objects.create(
            user=user,
            phone=phone,
            home_address=location,
            work_address=extra_detail,
            portal_role=portal_type
        )
        user_profile.save()

        messages.success(request, f"Registration successful for {portal_type.title()} Portal! You can now log in.")
        return redirect('portal_login', portal_type=portal_type)

    return render(request, 'portal_register.html', {'portal_type': portal_type})



def portal_logout_view(request):
    if 'portal_role' in request.session:
        del request.session['portal_role']
    logout(request)
    return redirect('home')


# --- Showroom Fleet Cars List ---

@login_required
def portal_rental_view(request):
    if request.session.get('portal_role') != 'rental':
        request.session['portal_role'] = 'rental'
    
    import datetime
    today = datetime.date.today()
    CarBooking.objects.filter(status='Approved', drop_date__lt=today).update(status='Completed')
    
    bookings = CarBooking.objects.all().order_by('-created_at')

    if request.method == "POST":
        action = request.POST.get('action')
        booking_id = request.POST.get('booking_id')
        if action == 'add_vehicle':
            v_name = request.POST.get('vehicle_name')
            v_type = request.POST.get('vehicle_type', 'sedan')
            try:
                v_price = float(request.POST.get('vehicle_price', 10000))
            except (ValueError, TypeError):
                v_price = 10000.0
            v_year = request.POST.get('vehicle_year', '2024')
            v_trans = request.POST.get('vehicle_trans', 'AUTO')
            v_fuel = request.POST.get('vehicle_fuel', 'Petrol')
            try:
                v_seats = int(request.POST.get('vehicle_seats', 5))
            except (ValueError, TypeError):
                v_seats = 5
            v_mileage = request.POST.get('vehicle_mileage', '12 kmpl')
            
            v_image = 'car-rent-1.png'
            if request.FILES.get('vehicle_image'):
                img_file = request.FILES['vehicle_image']
                import os
                from django.conf import settings
                media_dir = os.path.join(settings.MEDIA_ROOT, 'custom_cars')
                os.makedirs(media_dir, exist_ok=True)
                save_path = os.path.join(media_dir, img_file.name)
                with open(save_path, 'wb+') as destination:
                    for chunk in img_file.chunks():
                        destination.write(chunk)
                v_image = f'/media/custom_cars/{img_file.name}'

            new_car = {
                'id': len(SHOWROOM_CARS) + random.randint(100, 999),
                'name': v_name,
                'price': v_price,
                'image': v_image,
                'year': v_year,
                'trans': v_trans,
                'mileage': v_mileage,
                'type': v_type,
                'seats': v_seats,
                'fuel': v_fuel
            }
            SHOWROOM_CARS.append(new_car)
            messages.success(request, f"New vehicle '{v_name}' successfully added to rental fleet inventory!")
            return redirect('portal_rental_cars')

        elif booking_id and action:
            try:
                booking_obj = CarBooking.objects.get(id=booking_id)
                if action == 'approve':
                    booking_obj.status = 'Approved'
                    booking_obj.save()
                    messages.success(request, f"Car booking RS-{booking_id} approved and confirmed.")
                elif action == 'cancel':
                    booking_obj.status = 'Cancelled'
                    booking_obj.save()
                    messages.warning(request, f"Car booking RS-{booking_id} cancelled.")
            except CarBooking.DoesNotExist:
                pass
            return redirect('portal_rental')

    # Statistics
    total_earnings = sum(b.total_price for b in bookings if b.status == 'Approved' or b.status == 'Completed')
    total_rented = bookings.filter(status='Approved').count()
    pending_approvals = bookings.filter(status='Pending').count()
    active_rentals = bookings.filter(status='Approved', pickup_date__lte=today).count()

    context = {
        'bookings': bookings[:5],  # Display latest 5 on overview dashboard
        'total_earnings': total_earnings,
        'total_rented': total_rented,
        'pending_approvals': pending_approvals,
        'active_rentals': active_rentals,
    }
    return render(request, 'portal_rental.html', context)



@login_required
def portal_rental_bookings_view(request):
    if request.session.get('portal_role') != 'rental':
        request.session['portal_role'] = 'rental'

    import datetime
    today = datetime.date.today()
    CarBooking.objects.filter(status='Approved', drop_date__lt=today).update(status='Completed')

    bookings = CarBooking.objects.all().order_by('-created_at')

    if request.method == "POST":
        action = request.POST.get('action')
        booking_id = request.POST.get('booking_id')
        if action == 'add_vehicle':
            v_name = request.POST.get('vehicle_name')
            v_type = request.POST.get('vehicle_type', 'sedan')
            try:
                v_price = float(request.POST.get('vehicle_price', 10000))
            except (ValueError, TypeError):
                v_price = 10000.0
            v_year = request.POST.get('vehicle_year', '2024')
            v_trans = request.POST.get('vehicle_trans', 'AUTO')
            v_fuel = request.POST.get('vehicle_fuel', 'Petrol')
            try:
                v_seats = int(request.POST.get('vehicle_seats', 5))
            except (ValueError, TypeError):
                v_seats = 5
            v_mileage = request.POST.get('vehicle_mileage', '12 kmpl')
            
            v_image = 'car-rent-1.png'
            if request.FILES.get('vehicle_image'):
                img_file = request.FILES['vehicle_image']
                import os
                from django.conf import settings
                media_dir = os.path.join(settings.MEDIA_ROOT, 'custom_cars')
                os.makedirs(media_dir, exist_ok=True)
                save_path = os.path.join(media_dir, img_file.name)
                with open(save_path, 'wb+') as destination:
                    for chunk in img_file.chunks():
                        destination.write(chunk)
                v_image = f'/media/custom_cars/{img_file.name}'

            new_car = {
                'id': len(SHOWROOM_CARS) + random.randint(100, 999),
                'name': v_name,
                'price': v_price,
                'image': v_image,
                'year': v_year,
                'trans': v_trans,
                'mileage': v_mileage,
                'type': v_type,
                'seats': v_seats,
                'fuel': v_fuel
            }
            SHOWROOM_CARS.append(new_car)
            messages.success(request, f"New vehicle '{v_name}' successfully added to rental fleet inventory!")
            return redirect('portal_rental_cars')

        elif booking_id and action:
            try:
                booking_obj = CarBooking.objects.get(id=booking_id)
                if action == 'approve':
                    booking_obj.status = 'Approved'
                    booking_obj.save()
                    messages.success(request, f"Car booking RS-{booking_id} approved and confirmed.")
                elif action == 'cancel':
                    booking_obj.status = 'Cancelled'
                    booking_obj.save()
                    messages.warning(request, f"Car booking RS-{booking_id} cancelled.")
                elif action == 'complete':
                    booking_obj.status = 'Completed'
                    booking_obj.save()
                    messages.success(request, f"Car booking RS-{booking_id} marked as completed and moved to Rides Completed page.")
            except CarBooking.DoesNotExist:
                pass
            return redirect('portal_rental_bookings')

    return render(request, 'portal_rental_bookings.html', {'bookings': bookings})



@login_required
def portal_rental_cars_view(request):
    if request.session.get('portal_role') != 'rental':
        request.session['portal_role'] = 'rental'

    import datetime
    today = datetime.date.today()
    CarBooking.objects.filter(status='Approved', drop_date__lt=today).update(status='Completed')

    # --- Handle ADD vehicle ---
    if request.method == "POST" and request.POST.get('action') == 'add_vehicle':
        v_name = request.POST.get('vehicle_name')
        v_type = request.POST.get('vehicle_type', 'sedan')
        try:
            v_price = float(request.POST.get('vehicle_price', 10000))
        except (ValueError, TypeError):
            v_price = 10000.0
        v_year = request.POST.get('vehicle_year', '2024')
        v_trans = request.POST.get('vehicle_trans', 'AUTO')
        v_fuel = request.POST.get('vehicle_fuel', 'Petrol')
        try:
            v_seats = int(request.POST.get('vehicle_seats', 5))
        except (ValueError, TypeError):
            v_seats = 5
        v_mileage = request.POST.get('vehicle_mileage', '12 kmpl')

        v_image = 'car-rent-1.png'
        if request.FILES.get('vehicle_image'):
            img_file = request.FILES['vehicle_image']
            import os
            from django.conf import settings
            media_dir = os.path.join(settings.MEDIA_ROOT, 'custom_cars')
            os.makedirs(media_dir, exist_ok=True)
            save_path = os.path.join(media_dir, img_file.name)
            with open(save_path, 'wb+') as destination:
                for chunk in img_file.chunks():
                    destination.write(chunk)
            v_image = f'/media/custom_cars/{img_file.name}'

        new_car = {
            'id': len(SHOWROOM_CARS) + random.randint(100, 999),
            'name': v_name,
            'price': v_price,
            'image': v_image,
            'year': v_year,
            'trans': v_trans,
            'mileage': v_mileage,
            'type': v_type,
            'seats': v_seats,
            'fuel': v_fuel
        }
        SHOWROOM_CARS.append(new_car)
        # Also un-remove it if it was previously removed
        RemovedCar.objects.filter(car_name=v_name).delete()
        messages.success(request, f"New vehicle '{v_name}' successfully added to rental fleet inventory!")
        return redirect('portal_rental_cars')

    # --- Handle REMOVE vehicle ---
    if request.method == "POST" and request.POST.get('action') == 'remove_vehicle':
        car_name = request.POST.get('car_name', '').strip()
        reason = request.POST.get('remove_reason', 'out_of_service')
        if car_name:
            RemovedCar.objects.get_or_create(
                car_name=car_name,
                defaults={'reason': reason, 'removed_by': request.user}
            )
            # Update reason if already exists
            RemovedCar.objects.filter(car_name=car_name).update(reason=reason)
            messages.warning(request, f"Vehicle '{car_name}' has been removed from the active fleet ({dict(RemovedCar.REASON_CHOICES).get(reason, reason)}).")
        return redirect('portal_rental_cars')

    # --- Get removed car names to exclude from catalog ---
    removed_car_names = set(RemovedCar.objects.values_list('car_name', flat=True))
    removed_cars_list = list(RemovedCar.objects.select_related('removed_by').order_by('-removed_at'))

    # Get active approved bookings
    active_bookings = CarBooking.objects.filter(status='Approved').order_by('-created_at')

    # Build a lookup for active bookings by car name
    bookings_lookup = {}
    for booking in active_bookings:
        if booking.car_name not in bookings_lookup:
            bookings_lookup[booking.car_name] = {
                'booking_id': booking.id,
                'client_name': f"{booking.first_name} {booking.last_name}",
                'pickup_date': booking.pickup_date,
                'pickup_time': booking.pickup_time,
                'drop_location': booking.drop_location,
                'status': booking.status,
                'is_in_use': booking.pickup_date <= today
            }

    # Enhance SHOWROOM_CARS with booking status — exclude removed cars
    enhanced_cars = []
    currently_booked_cars = []
    currently_used_cars = []

    for car in SHOWROOM_CARS:
        if car['name'] in removed_car_names:
            continue  # skip removed vehicles
        car_copy = car.copy()
        booking_info = bookings_lookup.get(car['name'])
        if booking_info:
            car_copy['booking'] = booking_info
            if booking_info['is_in_use']:
                currently_used_cars.append(car_copy)
            else:
                currently_booked_cars.append(car_copy)
        enhanced_cars.append(car_copy)

    # Filter/group cars by category
    categories = {
        'Premium / Luxury': [c for c in enhanced_cars if c['type'] == 'sedan' and c['fuel'] != 'Electric'],
        'SUVs': [c for c in enhanced_cars if c['type'] == 'suv'],
        'EV / Electric': [c for c in enhanced_cars if c['fuel'] == 'Electric'],
        'Sports': [c for c in enhanced_cars if c['type'] == 'sports']
    }

    active_fleet = len(enhanced_cars)
    context = {
        'cars': enhanced_cars,
        'categories': categories,
        'currently_booked': currently_booked_cars,
        'currently_used': currently_used_cars,
        'total_fleet': active_fleet,
        'total_booked': len(currently_booked_cars),
        'total_used': len(currently_used_cars),
        'total_available': active_fleet - len(currently_booked_cars) - len(currently_used_cars),
        'removed_cars': removed_cars_list,
    }

    return render(request, 'portal_rental_cars.html', context)



@login_required
def portal_rental_remaining_view(request):

    if request.session.get('portal_role') != 'rental':
        request.session['portal_role'] = 'rental'

    import datetime
    today = datetime.date.today()
    CarBooking.objects.filter(status='Approved', drop_date__lt=today).update(status='Completed')

    # Get all approved bookings (these are "rented out" vehicles)
    approved_bookings = CarBooking.objects.filter(status='Approved').order_by('-created_at')
    rented_car_names = set(approved_bookings.values_list('car_name', flat=True))

    # Build rented_cars list from actual DB bookings (includes all user-booked vehicles)
    rented_cars = []
    for booking in approved_bookings:
        # Look for matching car in SHOWROOM_CARS for image/details
        car_details = next((c for c in SHOWROOM_CARS if c['name'] == booking.car_name), None)
        rented_cars.append({
            'name': booking.car_name,
            'image': car_details['image'] if car_details else booking.car_image,
            'price': car_details['price'] if car_details else booking.car_price,
            'type': car_details.get('type', 'sedan') if car_details else 'sedan',
            'trans': car_details.get('trans', 'AUTO') if car_details else 'AUTO',
            'client': f"{booking.first_name} {booking.last_name}",
            'mobile': booking.mobile_number,
            'pickup_date': booking.pickup_date,
            'drop_date': booking.drop_date,
            'total_price': booking.total_price,
            'booking_id': booking.id,
        })

    # Available cars = those in SHOWROOM_CARS NOT currently booked
    available_cars = [car for car in SHOWROOM_CARS if car['name'] not in rented_car_names]

    context = {
        'available_cars': available_cars,
        'rented_cars': rented_cars,
    }
    return render(request, 'portal_rental_remaining.html', context)


@login_required
def portal_rental_profile_view(request):
    if request.session.get('portal_role') != 'rental':
        request.session['portal_role'] = 'rental'

    import datetime
    today = datetime.date.today()
    CarBooking.objects.filter(status='Approved', drop_date__lt=today).update(status='Completed')

    # Get or create UserProfile for the admin
    user_profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Save profile image if uploaded
        if 'profile_image' in request.FILES:
            user_profile.profile_image = request.FILES['profile_image']

        # Save phone and location from form
        phone = request.POST.get('phone', '').strip()
        location = request.POST.get('location', '').strip()
        if phone:
            user_profile.phone = phone
        if location:
            user_profile.home_address = location

        # Save first/last name
        full_name = request.POST.get('full_name', '').strip()
        if full_name:
            parts = full_name.split(' ', 1)
            request.user.first_name = parts[0]
            request.user.last_name = parts[1] if len(parts) > 1 else ''
            request.user.save()

        # Save email
        email = request.POST.get('email', '').strip()
        if email:
            request.user.email = email
            request.user.save()

        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('portal_rental_profile')

    total_bookings = CarBooking.objects.count()
    approved_bookings = CarBooking.objects.filter(status='Approved').count()
    completed_bookings = CarBooking.objects.filter(status='Completed').count()
    pending_bookings = CarBooking.objects.filter(status='Pending').count()
    total_fleet = len(SHOWROOM_CARS)
    rented_count = CarBooking.objects.filter(status='Approved').values('car_name').distinct().count()
    available_count = max(0, total_fleet - rented_count)
    total_revenue = sum(b.total_price for b in CarBooking.objects.filter(status__in=['Approved', 'Completed']))

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'today': today,
        'total_bookings': total_bookings,
        'approved_bookings': approved_bookings,
        'completed_bookings': completed_bookings,
        'pending_bookings': pending_bookings,
        'total_fleet': total_fleet,
        'rented_count': rented_count,
        'available_count': available_count,
        'total_revenue': total_revenue,
    }
    return render(request, 'portal_rental_profile.html', context)


@login_required
def portal_rider_profile_view(request):
    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'
        
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if not user_profile:
        user_profile = UserProfile.objects.create(user=request.user)
        
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'save_image':
            cropped_data = request.POST.get('cropped_image_data')
            if cropped_data and ';base64,' in cropped_data:
                import base64
                from django.core.files.base import ContentFile
                try:
                    format, imgstr = cropped_data.split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr), name=f"user_{request.user.id}_profile.{ext}")
                    user_profile.image = data
                    user_profile.save()
                    messages.success(request, "Rider profile image updated successfully!")
                except Exception as e:
                    messages.error(request, f"Error cropping/saving image: {str(e)}")
            elif 'profile_image' in request.FILES:
                user_profile.image = request.FILES['profile_image']
                user_profile.save()
                messages.success(request, "Rider profile image uploaded successfully!")
            return redirect('portal_rider_profile')
            
        elif action == 'save_details':
            full_name = request.POST.get('full_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            location = request.POST.get('location')
            
            if full_name and ' ' in full_name:
                parts = full_name.split(' ', 1)
                request.user.first_name = parts[0]
                request.user.last_name = parts[1]
            elif full_name:
                request.user.first_name = full_name
                request.user.last_name = ""
                
            if email:
                request.user.email = email
            request.user.save()
            
            if phone:
                user_profile.mobile_number = phone
            if location:
                user_profile.location = location
            user_profile.save()
            
            messages.success(request, "Rider account details updated successfully!")
            return redirect('portal_rider_profile')
            
        elif action == 'save_security':
            current_pass = request.POST.get('current_password')
            new_pass = request.POST.get('new_password')
            confirm_pass = request.POST.get('confirm_password')
            
            if current_pass and new_pass and confirm_pass:
                if new_pass != confirm_pass:
                    messages.error(request, "New passwords do not match!")
                elif not request.user.check_password(current_pass):
                    messages.error(request, "Incorrect current password!")
                else:
                    request.user.set_password(new_pass)
                    request.user.save()
                    from django.contrib.auth import update_session_auth_hash
                    update_session_auth_hash(request, request.user)
                    messages.success(request, "Password updated successfully!")
            else:
                messages.error(request, "All password fields are required!")
            return redirect('portal_rider_profile')
            
        elif action == 'save_advanced':
            license_number = request.POST.get('license_number')
            if license_number:
                user_profile.work_address = license_number
                user_profile.save()
            messages.success(request, "Advanced rider settings updated successfully!")
            return redirect('portal_rider_profile')
            
        elif action == 'reset_avatar':
            user_profile.profile_image = None
            user_profile.save()
            messages.success(request, "Profile avatar reset successfully!")
            return redirect('portal_rider_profile')
            
        elif action == 'reset_fields':
            user_profile.phone = ""
            user_profile.home_address = ""
            user_profile.work_address = ""
            user_profile.save()
            messages.success(request, "Rider profile fields reset successfully!")
            return redirect('portal_rider_profile')
            
    past_trips = TaxiRideRequest.objects.filter(driver_name=request.user.username, status='Completed')
    total_trips = past_trips.count()
    total_earnings = sum(t.price for t in past_trips)
    
    context = {
        'user': request.user,
        'user_profile': user_profile,
        'total_trips': total_trips,
        'total_earnings': total_earnings,
    }
    return render(request, 'portal_rider_profile.html', context)


@login_required
def portal_carpool_profile_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'
        
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if not user_profile:
        user_profile = UserProfile.objects.create(user=request.user)
        
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'save_image':
            cropped_data = request.POST.get('cropped_image_data')
            if cropped_data and ';base64,' in cropped_data:
                import base64
                from django.core.files.base import ContentFile
                try:
                    format, imgstr = cropped_data.split(';base64,')
                    ext = format.split('/')[-1]
                    data = ContentFile(base64.b64decode(imgstr), name=f"user_{request.user.id}_profile.{ext}")
                    user_profile.image = data
                    user_profile.save()
                    messages.success(request, "Pooling host profile image updated successfully!")
                except Exception as e:
                    messages.error(request, f"Error cropping/saving image: {str(e)}")
            elif 'profile_image' in request.FILES:
                user_profile.image = request.FILES['profile_image']
                user_profile.save()
                messages.success(request, "Pooling host profile image uploaded successfully!")
            return redirect('portal_carpool_profile')
            
        elif action == 'save_details':
            full_name = request.POST.get('full_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            location = request.POST.get('location')
            
            if full_name and ' ' in full_name:
                parts = full_name.split(' ', 1)
                request.user.first_name = parts[0]
                request.user.last_name = parts[1]
            elif full_name:
                request.user.first_name = full_name
                request.user.last_name = ""
                
            if email:
                request.user.email = email
            request.user.save()
            
            if phone:
                user_profile.mobile_number = phone
            if location:
                user_profile.location = location
            user_profile.save()
            
            messages.success(request, "Pooling host personal details updated successfully!")
            return redirect('portal_carpool_profile')
            
        elif action == 'save_security':
            current_pass = request.POST.get('current_password')
            new_pass = request.POST.get('new_password')
            confirm_pass = request.POST.get('confirm_password')
            
            if current_pass and new_pass and confirm_pass:
                if new_pass != confirm_pass:
                    messages.error(request, "New passwords do not match!")
                elif not request.user.check_password(current_pass):
                    messages.error(request, "Incorrect current password!")
                else:
                    request.user.set_password(new_pass)
                    request.user.save()
                    from django.contrib.auth import update_session_auth_hash
                    update_session_auth_hash(request, request.user)
                    messages.success(request, "Password updated successfully!")
            else:
                messages.error(request, "All password fields are required!")
            return redirect('portal_carpool_profile')
            
        elif action == 'save_advanced':
            license_number = request.POST.get('license_number')
            if license_number:
                user_profile.work_address = license_number
                user_profile.save()
            messages.success(request, "Advanced host settings updated successfully!")
            return redirect('portal_carpool_profile')
            
        elif action == 'reset_avatar':
            user_profile.profile_image = None
            user_profile.save()
            messages.success(request, "Profile avatar reset successfully!")
            return redirect('portal_carpool_profile')
            
        elif action == 'reset_fields':
            user_profile.phone = ""
            user_profile.home_address = ""
            user_profile.work_address = ""
            user_profile.save()
            messages.success(request, "Profile settings and fields reset successfully!")
            return redirect('portal_carpool_profile')
            
    user_offers = CarpoolOffer.objects.filter(host=request.user)
    total_routes = user_offers.count()
    
    context = {
        'user': request.user,
        'user_profile': user_profile,
        'total_routes': total_routes,
    }
    return render(request, 'portal_carpool_profile.html', context)




@login_required
def portal_rental_completed_view(request):
    if request.session.get('portal_role') != 'rental':
        request.session['portal_role'] = 'rental'

    import datetime
    today = datetime.date.today()
    CarBooking.objects.filter(status='Approved', drop_date__lt=today).update(status='Completed')

    bookings = CarBooking.objects.filter(status='Completed').order_by('-drop_date')
    return render(request, 'portal_rental_completed.html', {'bookings': bookings})



@login_required
def portal_rider_view(request):
    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'

    from django.db.models import Avg, Sum
    from django.utils import timezone

    # Display active/pending requests
    pending_rides = TaxiRideRequest.objects.filter(status='Pending').order_by('-created_at')
    
    # If the current rider has an active accepted ride
    active_ride = TaxiRideRequest.objects.filter(
        driver_name=request.user.username,
        status__in=['Accepted', 'Arrived', 'In_Progress']
    ).first()

    # Past completed trips by this rider
    past_trips = TaxiRideRequest.objects.filter(
        driver_name=request.user.username,
        status='Completed'
    ).order_by('-created_at')

    # Cancelled trips by this rider
    cancelled_trips = TaxiRideRequest.objects.filter(
        driver_name=request.user.username,
        status='Cancelled'
    ).count()

    # Today's earnings
    today = timezone.now().date()
    today_trips = past_trips.filter(created_at__date=today)
    today_earnings = sum(t.price for t in today_trips)

    # Statistics
    total_trips = past_trips.count()
    total_gross = sum(t.price for t in past_trips)
    platform_fee = round(total_gross * 0.10, 2)   # 10% commission
    net_payout = round(total_gross - platform_fee, 2)
    
    rated_rides = past_trips.filter(rating__isnull=False, rating__gt=0)
    avg_rating_val = rated_rides.aggregate(Avg('rating'))['rating__avg']
    rating = round(float(avg_rating_val), 1) if avg_rating_val else 5.0

    # Recent 5 completed trips for overview feed
    recent_trips = past_trips[:5]

    context = {
        'pending_rides': pending_rides,
        'active_ride': active_ride,
        'total_trips': total_trips,
        'total_earnings': total_gross,
        'platform_fee': platform_fee,
        'net_payout': net_payout,
        'cancelled_trips': cancelled_trips,
        'today_earnings': today_earnings,
        'rating': rating,
        'recent_trips': recent_trips,
    }
    return render(request, 'portal_rider.html', context)



@login_required
def portal_rider_active_view(request):
    from django.db.models import Q
    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'

    active_ride = TaxiRideRequest.objects.filter(
        driver_name=request.user.username
    ).filter(
        Q(status__in=['Accepted', 'Arrived', 'In_Progress']) | Q(status='Completed', cancel_reason='payment_pending')
    ).first()

    return render(request, 'portal_rider_active.html', {'active_ride': active_ride})



@login_required
def portal_rider_earnings_view(request):
    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'

    from django.utils import timezone

    past_trips = TaxiRideRequest.objects.filter(
        driver_name=request.user.username,
        status='Completed'
    ).order_by('-created_at')

    total_earnings = sum(t.price for t in past_trips)
    platform_fee = round(total_earnings * 0.10, 2)  # 10% commission fee
    net_payout = round(total_earnings - platform_fee, 2)

    # Per-trip breakdown for table
    trips_with_fees = []
    for t in past_trips:
        fee = round(t.price * 0.10, 2)
        net = round(t.price - fee, 2)
        trips_with_fees.append({
            'trip': t,
            'gross': t.price,
            'platform_fee': fee,
            'net': net,
        })

    # This week earnings
    today = timezone.now().date()
    start_of_week = today - timezone.timedelta(days=today.weekday())
    week_trips = past_trips.filter(created_at__date__gte=start_of_week)
    week_earnings = sum(t.price for t in week_trips)

    # Today earnings
    today_trips = past_trips.filter(created_at__date=today)
    today_earnings = sum(t.price for t in today_trips)

    context = {
        'trips': past_trips,
        'trips_with_fees': trips_with_fees,
        'total_earnings': total_earnings,
        'platform_fee': platform_fee,
        'net_payout': net_payout,
        'week_earnings': week_earnings,
        'today_earnings': today_earnings,
        'total_trips': past_trips.count(),
    }
    return render(request, 'portal_rider_earnings.html', context)



@login_required
def portal_rider_trips_view(request):
    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'

    trips = TaxiRideRequest.objects.filter(
        driver_name=request.user.username
    ).order_by('-created_at')

    return render(request, 'portal_rider_trips.html', {'trips': trips})



@login_required
def portal_carpool_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    offers = CarpoolOffer.objects.filter(host=request.user).order_by('-created_at')
    
    # Calculate statistics
    total_offers = offers.count()
    total_passengers = CarpoolSeatBooking.objects.filter(carpool__host=request.user).count()
    active_seats = sum(o.available_seats for o in offers)
    fuel_saved_split = total_passengers * 450.0 # split estimate

    context = {
        'offers': offers[:3], # show latest 3
        'total_offers': total_offers,
        'total_passengers': total_passengers,
        'active_seats': active_seats,
        'fuel_saved_split': fuel_saved_split,
    }
    return render(request, 'portal_carpool.html', context)



@login_required
def portal_carpool_publish_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    if request.method == "POST":
        vehicle_name = request.POST.get('vehicle_name')
        vehicle_number = request.POST.get('vehicle_number')
        start = request.POST.get('start_location')
        dest = request.POST.get('destination')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        seats = int(request.POST.get('seats', 4))
        vehicle_type = request.POST.get('vehicle_type', 'car')
        price = int(request.POST.get('price', 0))

        if vehicle_name and start and dest and date_str:
            CarpoolOffer.objects.create(
                host=request.user,
                vehicle_name=vehicle_name,
                vehicle_number=vehicle_number,
                start_location=start,
                destination=dest,
                date=datetime.strptime(date_str, '%Y-%m-%d').date(),
                time=time_str if time_str else "09:00",
                total_seats=seats,
                available_seats=seats,
                vehicle_type=vehicle_type,
                price=price
            )
            messages.success(request, f"Successfully published travel plan from {start} to {dest}!")
            return redirect('portal_carpool_itineraries')

    return render(request, 'portal_carpool_publish.html')



@login_required
def portal_carpool_itineraries_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    offers = CarpoolOffer.objects.filter(host=request.user).exclude(status__in=['Completed', 'Cancelled']).order_by('-created_at')
    return render(request, 'portal_carpool_itineraries.html', {'offers': offers})



@login_required
def portal_carpool_bookings_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    bookings = CarpoolSeatBooking.objects.filter(carpool__host=request.user).order_by('-booked_at')

    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        action = request.POST.get('action')
        if booking_id and action:
            try:
                booking = CarpoolSeatBooking.objects.get(id=booking_id)
                carpool = booking.carpool
                if action == 'approve':
                    if carpool.available_seats >= booking.seats_booked:
                        booking.status = 'Approved'
                        booking.save()
                        carpool.available_seats -= booking.seats_booked
                        carpool.save()
                        messages.success(request, f"Approved seat request for {booking.user.username}. Chat is now unlocked!")
                    else:
                        messages.error(request, "Cannot approve. No available seats remaining.")
                elif action == 'cancel':
                    if booking.status == 'Approved':
                        carpool.available_seats += booking.seats_booked
                        carpool.save()
                    booking.status = 'Cancelled'
                    booking.save()
                    messages.warning(request, f"Cancelled seat booking request for {booking.user.username}.")
            except CarpoolSeatBooking.DoesNotExist:
                pass
            return redirect('portal_carpool_bookings')

    return render(request, 'portal_carpool_bookings.html', {'bookings': bookings})


# --- AJAX API Endpoints for Real-Time scenario ---


@login_required
def api_request_ride(request):
    if request.method == "POST":
        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')
        distance = float(request.POST.get('distance', 5.0))
        price = round(distance * 15, 2) # Price calculation rounded to 2 decimal places
        
        # Generate 4-digit PIN
        pin = str(random.randint(1000, 9999))
        
        ride = TaxiRideRequest.objects.create(
            user=request.user,
            pickup=pickup,
            drop=drop,
            distance=distance,
            price=price,
            pin=pin,
            status='Pending'
        )
        return JsonResponse({
            'success': True,
            'ride_id': ride.id,
            'pin': pin,
            'status': ride.status,
            'message': 'Searching for nearby riders...'
        })
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def api_check_ride_status(request, ride_id):
    try:
        ride = TaxiRideRequest.objects.get(id=ride_id)
        
        # Auto-cancel if pending for more than 5 minutes (300 seconds)
        if ride.status == 'Pending':
            from django.utils import timezone
            elapsed = (timezone.now() - ride.created_at).total_seconds()
            if elapsed > 300:
                ride.status = 'Cancelled'
                ride.save()

        driver_rating = 5.0
        if ride.driver_name:
            from django.db.models import Avg
            avg_rating = TaxiRideRequest.objects.filter(driver_name=ride.driver_name, rating__isnull=False, rating__gt=0).aggregate(Avg('rating'))['rating__avg']
            if avg_rating is not None:
                driver_rating = round(float(avg_rating), 1)

        return JsonResponse({
            'success': True,
            'ride_id': ride.id,
            'status': ride.status,
            'driver_name': ride.driver_name or 'Searching...',
            'driver_rating': driver_rating,
            'pin': ride.pin,
            'pickup': ride.pickup,
            'drop': ride.drop,
            'price': ride.price,
            'payment_status': ride.cancel_reason or 'payment_pending'
        })
    except TaxiRideRequest.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Ride request not found.'})



@login_required
def api_accept_ride(request, ride_id):
    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'

    try:
        ride = TaxiRideRequest.objects.get(id=ride_id)
        if ride.status != 'Pending':
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
                return JsonResponse({
                    'success': False,
                    'message': 'Ride already accepted or processed by another driver.'
                })
            from django.contrib import messages
            messages.warning(request, 'Ride already accepted or processed by another driver.')
            return redirect('portal_rider')

        # Accept the ride
        ride.driver_name = request.user.username
        ride.status = 'Accepted'
        ride.save()

        # Redirect standard form POST, return JSON for fetch/AJAX
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
            return JsonResponse({
                'success': True,
                'ride_id': ride.id,
                'status': ride.status,
                'message': f'Ride accepted successfully! Please head to {ride.pickup}.'
            })
        return redirect('portal_rider_active')
    except TaxiRideRequest.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Ride not found.'})



@login_required
def api_update_ride_status(request, ride_id):
    from django.contrib import messages
    from django.shortcuts import redirect

    if request.session.get('portal_role') != 'rider':
        request.session['portal_role'] = 'rider'

    try:
        ride = TaxiRideRequest.objects.get(id=ride_id)
        if ride.driver_name != request.user.username:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                return JsonResponse({'success': False, 'message': 'Unauthorized action.'})
            else:
                messages.error(request, 'Unauthorized action.')
                return redirect('portal_rider_active')

        # Accept action or status in any case format
        action = request.POST.get('action') or request.POST.get('status')
        if action:
            action = action.lower()

        if action in ['arrive', 'arrived']:
            ride.status = 'Arrived'
            ride.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                return JsonResponse({'success': True, 'status': ride.status})
            else:
                messages.success(request, 'You have arrived at the pickup location.')
                return redirect('portal_rider_active')
        
        elif action in ['start', 'in_progress']:
            entered_pin = request.POST.get('pin')
            if not entered_pin:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                    return JsonResponse({'success': False, 'message': 'PIN is required to start the ride.'})
                else:
                    messages.error(request, 'PIN is required to start the ride.')
                    return redirect('portal_rider_active')
            
            if entered_pin == ride.pin:
                ride.status = 'In_Progress'
                ride.save()
                if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                    return JsonResponse({'success': True, 'status': ride.status})
                else:
                    messages.success(request, 'Ride started successfully! Safe travels.')
                    return redirect('portal_rider_active')
            else:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                    return JsonResponse({'success': False, 'message': 'Invalid PIN! Please check with the passenger.'})
                else:
                    messages.error(request, 'Invalid PIN! Please ask the passenger for their correct 4-digit PIN.')
                    return redirect('portal_rider_active')
        
        elif action in ['complete', 'completed']:
            ride.status = 'Completed'
            ride.cancel_reason = 'payment_pending'
            ride.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                return JsonResponse({'success': True, 'status': ride.status, 'payment_status': ride.cancel_reason})
            else:
                messages.success(request, 'Destination reached! Please select payment method.')
                return redirect('portal_rider_active')
        
        elif action in ['confirm_payment', 'payment_completed']:
            ride.status = 'Completed'
            ride.cancel_reason = 'payment_completed'
            ride.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
                return JsonResponse({'success': True, 'status': ride.status, 'payment_status': ride.cancel_reason})
            else:
                messages.success(request, 'Payment confirmed! Ride completed successfully.')
                return redirect('portal_rider_active')

        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
            return JsonResponse({'success': False, 'message': 'Invalid action.'})
        else:
            messages.error(request, 'Invalid status action requested.')
            return redirect('portal_rider_active')

    except TaxiRideRequest.DoesNotExist:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == 'true':
            return JsonResponse({'success': False, 'message': 'Ride not found.'})
        else:
            messages.error(request, 'Ride not found.')
            return redirect('portal_rider_active')


@login_required
def api_cancel_ride(request, ride_id):
    try:
        ride = TaxiRideRequest.objects.get(id=ride_id)
        if ride.user != request.user and ride.driver_name != request.user.username:
            return JsonResponse({'success': False, 'message': 'Unauthorized action.'})
        
        reason = request.POST.get('reason')
        if reason:
            ride.cancel_reason = reason
        
        ride.status = 'Cancelled'
        ride.save()
        return JsonResponse({'success': True, 'message': 'Ride cancelled successfully.'})
    except TaxiRideRequest.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Ride not found.'})


@login_required
def api_book_carpool_seat(request, carpool_id):
    try:
        carpool = CarpoolOffer.objects.get(id=carpool_id)
        
        # Parse custom seats count request from POST
        seats_booked = int(request.POST.get('seats_booked', 1))
        
        if carpool.available_seats < seats_booked:
            return JsonResponse({'success': False, 'message': f'Not enough available seats left. Only {carpool.available_seats} remaining.'})

        # Prevent double booking
        if CarpoolSeatBooking.objects.filter(carpool=carpool, user=request.user).exists():
            return JsonResponse({'success': False, 'message': 'You have already requested a seat on this carpool!'})

        # Create booking in Pending status
        CarpoolSeatBooking.objects.create(
            carpool=carpool,
            user=request.user,
            seats_booked=seats_booked,
            status='Pending'
        )
        return JsonResponse({
            'success': True,
            'message': f'Request for {seats_booked} seat(s) sent to host driver! Please wait for approval.'
        })
    except CarpoolOffer.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Carpool offer not found.'})


def get_carpool_offers(request):
    offers = CarpoolOffer.objects.filter(available_seats__gt=0).order_by('date')
    start_q = request.GET.get('start')
    dest_q = request.GET.get('destination')
    if start_q:
        offers = offers.filter(start_location__icontains=start_q)
    if dest_q:
        offers = offers.filter(destination__icontains=dest_q)

    data = []
    for o in offers:
        data.append({
            'id': o.id,
            'host': o.host.username,
            'vehicle': o.vehicle_name,
            'route': f"{o.start_location} → {o.destination}",
            'date': o.date.strftime('%Y-%m-%d'),
            'time': o.time.strftime('%H:%M'),
            'seats': o.available_seats
        })
    return JsonResponse({'success': True, 'offers': data})



def user_carpools_view(request):
    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
    offers = CarpoolOffer.objects.all().order_by('-created_at')
    
    start = request.GET.get('start', '')
    dest = request.GET.get('destination', '')
    if start:
        offers = offers.filter(start_location__icontains=start)
    if dest:
        offers = offers.filter(destination__icontains=dest)

    my_bookings = CarpoolSeatBooking.objects.filter(user=request.user).order_by('-booked_at')

    context = {
        'offers': offers,
        'my_bookings': my_bookings,
        'start_query': start,
        'dest_query': dest,
    }
    return render(request, 'user_carpools.html', context)



@login_required
def api_submit_feedback(request, ride_id):
    if request.method == "POST":
        try:
            ride = TaxiRideRequest.objects.get(id=ride_id, user=request.user)
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback', '')
            if rating:
                ride.rating = int(rating)
            if feedback:
                ride.feedback = feedback
            ride.save()
            return JsonResponse({'success': True, 'message': 'Feedback submitted successfully.'})
        except TaxiRideRequest.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Ride not found.'})
        except ValueError:
            return JsonResponse({'success': False, 'message': 'Invalid rating value.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



def passenger_settings_view(request):
    from django.db.models import Sum, Avg
    from django.contrib.auth import update_session_auth_hash
    from django.utils import timezone
    from django.urls import reverse

    if not request.user.is_authenticated:
        return redirect('/?show_auth_warning=1')
        
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form_action = request.POST.get('form_action')
        
        if form_action == 'upload_photo':
            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
                profile.save()
                messages.success(request, 'Profile photo updated successfully!')
            else:
                messages.warning(request, 'No image file was provided.')
            return redirect(reverse('passenger_settings') + '#profile')
            
        elif form_action == 'rename':
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            new_username = request.POST.get('username', '').strip()
            
            if new_username:
                if ' ' in new_username:
                    messages.error(request, 'Username cannot contain spaces.')
                elif User.objects.filter(username=new_username).exclude(id=request.user.id).exists():
                    messages.error(request, 'This username is already taken.')
                else:
                    request.user.username = new_username
                    request.user.first_name = first_name
                    request.user.last_name = last_name
                    request.user.save()
                    messages.success(request, 'Name and username updated successfully!')
            else:
                messages.error(request, 'Username is required.')
            return redirect(reverse('passenger_settings') + '#profile')
            
        elif form_action == 'account_settings':
            email = request.POST.get('email', '').strip()
            phone = request.POST.get('phone', '').strip()
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if email:
                request.user.email = email
                request.user.save()
            
            profile.phone = phone
            profile.save()
            
            if password:
                if password != confirm_password:
                    messages.error(request, 'Passwords do not match.')
                else:
                    request.user.set_password(password)
                    request.user.save()
                    update_session_auth_hash(request, request.user)
                    messages.success(request, 'Password updated successfully!')
            
            messages.success(request, 'Account credentials updated successfully!')
            return redirect(reverse('passenger_settings') + '#security')
            
        elif form_action == 'favorite_locations':
            home_address = request.POST.get('home_address', '').strip()
            work_address = request.POST.get('work_address', '').strip()
            
            profile.home_address = home_address
            profile.work_address = work_address
            profile.save()
            
            messages.success(request, 'Saved places updated successfully!')
            return redirect(reverse('passenger_settings') + '#locations')
            
    # Calculate statistics for the GET request
    total_rides = TaxiRideRequest.objects.filter(user=request.user).count()
    completed_rides = TaxiRideRequest.objects.filter(user=request.user, status='Completed').count()
    cancelled_rides = TaxiRideRequest.objects.filter(user=request.user, status='Cancelled').count()
    
    total_spent = TaxiRideRequest.objects.filter(user=request.user, status='Completed').aggregate(Sum('price'))['price__sum'] or 0.0
    total_spent = round(total_spent, 2)
    
    total_distance = TaxiRideRequest.objects.filter(user=request.user, status='Completed').aggregate(Sum('distance'))['distance__sum'] or 0.0
    total_distance = round(total_distance, 1)
    
    avg_rating = TaxiRideRequest.objects.filter(user=request.user, status='Completed', rating__isnull=False).aggregate(Avg('rating'))['rating__avg']
    avg_rating = round(avg_rating, 1) if avg_rating else None
    
    recent_ride = TaxiRideRequest.objects.filter(user=request.user).order_by('-created_at').first()
    member_since = request.user.date_joined.strftime('%B %d, %Y')
    account_age_days = (timezone.now() - request.user.date_joined).days
    last_login = request.user.last_login.strftime('%B %d, %Y, %I:%M %p') if request.user.last_login else "—"

    context = {
        'profile': profile,
        'total_rides': total_rides,
        'completed_rides': completed_rides,
        'cancelled_rides': cancelled_rides,
        'total_spent': total_spent,
        'total_distance': total_distance,
        'avg_rating': avg_rating,
        'recent_ride': recent_ride,
        'member_since': member_since,
        'account_age_days': account_age_days,
        'last_login': last_login,
    }
    return render(request, 'passenger_settings.html', context)


@login_required
def portal_carpool_completed_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    import datetime
    today = datetime.date.today()

    # Completed hosted offers: date < today or status in ['Completed', 'Cancelled']
    completed_offers = CarpoolOffer.objects.filter(
        host=request.user
    ).filter(
        Q(date__lt=today) | Q(status__in=['Completed', 'Cancelled'])
    ).order_by('-date', '-time')

    # Incompleted / Active / Upcoming hosted offers: date >= today and status not in ['Completed', 'Cancelled']
    upcoming_offers = CarpoolOffer.objects.filter(
        host=request.user
    ).exclude(
        status__in=['Completed', 'Cancelled']
    ).filter(
        date__gte=today
    ).order_by('date', 'time')

    # Totals/stats for the user:
    total_hosted = CarpoolOffer.objects.filter(host=request.user).count()
    total_completed = completed_offers.count()
    total_upcoming = upcoming_offers.count()
    
    total_passengers = CarpoolSeatBooking.objects.filter(
        carpool__host=request.user,
        status='Approved'
    ).count()

    context = {
        'completed_offers': completed_offers,
        'upcoming_offers': upcoming_offers,
        'total_hosted': total_hosted,
        'total_completed': total_completed,
        'total_upcoming': total_upcoming,
        'total_passengers': total_passengers,
        'today': today,
    }
    return render(request, 'portal_carpool_completed.html', context)


@login_required
def portal_carpool_active_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    import datetime
    today = datetime.date.today()

    # Find active ride (status='In_Progress') or next upcoming ride today/future
    active_pool = CarpoolOffer.objects.filter(
        host=request.user,
        status='In_Progress'
    ).first()

    if not active_pool:
        # Get next upcoming pool
        active_pool = CarpoolOffer.objects.filter(
            host=request.user,
            status='Upcoming',
            date__gte=today
        ).order_by('date', 'time').first()

    bookings = []
    if active_pool:
        bookings = CarpoolSeatBooking.objects.filter(
            carpool=active_pool,
            status='Approved'
        )

    context = {
        'active_pool': active_pool,
        'bookings': bookings,
    }
    return render(request, 'portal_carpool_active.html', context)


@login_required
def portal_carpool_chats_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    # Get bookings on user's carpools to find chat partners
    bookings = CarpoolSeatBooking.objects.filter(
        carpool__host=request.user,
        status='Approved'
    ).select_related('user', 'carpool').order_by('-booked_at')

    # Group by passenger to show unique chat users
    unique_passengers = {}
    for b in bookings:
        p_username = b.user.username
        if p_username not in unique_passengers:
            unique_passengers[p_username] = {
                'user': b.user,
                'last_booking': b
            }

    context = {
        'chat_partners': unique_passengers.values(),
    }
    return render(request, 'portal_carpool_chats.html', context)


@login_required
def portal_carpool_analytics_view(request):
    if request.session.get('portal_role') != 'carpool':
        request.session['portal_role'] = 'carpool'

    offers = CarpoolOffer.objects.filter(host=request.user)
    total_rides = offers.count()
    completed_rides = offers.filter(status='Completed').count()
    
    total_passengers = CarpoolSeatBooking.objects.filter(
        carpool__host=request.user,
        status='Approved'
    ).count()

    co2_saved = round(total_passengers * 15.0 * 0.45, 1) # in kg
    fuel_saved = round(total_passengers * 15.0 / 12.0, 1) # in gallons, assuming 12km/liter
    money_earned = total_passengers * 450.0 # assume flat 450 per seat split

    # Mock reviews/ratings
    avg_rating = 4.8 if total_rides > 0 else 5.0

    context = {
        'total_rides': total_rides,
        'completed_rides': completed_rides,
        'total_passengers': total_passengers,
        'co2_saved': co2_saved,
        'fuel_saved': fuel_saved,
        'money_earned': money_earned,
        'avg_rating': avg_rating,
    }
    return render(request, 'portal_carpool_analytics.html', context)


@login_required
def api_update_carpool_status(request, carpool_id):
    if request.method == "POST":
        try:
            carpool = CarpoolOffer.objects.get(id=carpool_id, host=request.user)
            action = request.POST.get('action')
            if action == 'start':
                carpool.status = 'In_Progress'
                carpool.save()
                return JsonResponse({'success': True, 'status': carpool.status, 'message': 'Ride is now active! Happy sharing.'})
            elif action == 'complete':
                carpool.status = 'Completed'
                carpool.save()
                return JsonResponse({'success': True, 'status': carpool.status, 'message': 'Ride completed successfully. Thank you!'})
            elif action == 'cancel':
                carpool.status = 'Cancelled'
                carpool.save()
                return JsonResponse({'success': True, 'status': carpool.status, 'message': 'Ride cancelled.'})
            return JsonResponse({'success': False, 'message': 'Invalid action.'})
        except CarpoolOffer.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Carpool not found.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def api_bulk_remove_carpools(request):
    if request.method == "POST":
        import json
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            if ids:
                CarpoolOffer.objects.filter(id__in=ids, host=request.user).update(status='Cancelled')
                return JsonResponse({'success': True, 'message': 'Selected plans successfully removed.'})
            return JsonResponse({'success': False, 'message': 'No plans selected.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})