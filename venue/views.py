from django.shortcuts import render, redirect
from .models import Hall, Apartment, Tenant, Tenancy, Accommodation, Payment, BusinessOwner

# View for displaying bookings
def get_bookings(request):
    halls = Hall.objects.all()
    apartments = Apartment.objects.all()

    context = {
        "halls": halls,
        "apartments": apartments,
        # Include other context variables as needed
    }
    return render(request, "venue/bookings.html", context)

# View for adding bookings
def add_bookings(request):
    if request.method == 'POST':
        # Retrieve data from the form
        accommodation_id = request.POST.get('hallAccommodationId')
        weddings = request.POST.get('weddings') == 'on'
        birthdays = request.POST.get('birthdays') == 'on'
        parties = request.POST.get('parties') == 'on'
        baby_shower = request.POST.get('babyShower') == 'on'
        corporate_events = request.POST.get('corporateEvents') == 'on'
        christmas = request.POST.get('christmas') == 'on'
        lifestyle_photoshoot = request.POST.get('lifestylePhotoshoot') == 'on'
        apartment_accommodation_id = request.POST.get('apartmentAccommodationId')
        check_in = request.POST.get('checkIn')
        check_out = request.POST.get('checkOut')
        guests = int(request.POST.get('guests'))
        rooms = int(request.POST.get('rooms'))
        apartment_availability = request.POST.get('apartmentAvailability')
        

        # Redirect to a success page or another view
        return redirect('get_bookings')  # Use the correct URL name for the bookings view

    return render(request, "venue/add_bookings.html")

