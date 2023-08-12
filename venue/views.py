from django.shortcuts import render
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
    return render(request, "venue/add_bookings.html")
