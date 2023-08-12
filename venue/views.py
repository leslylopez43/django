from .models import Hall, Apartment, Tenant, Tenancy, Accommodation, Payment, BusinessOwner
from django.shortcuts import render

# Create your views here.
def get_bookings(request):
	return render(request, "venue/bookings.html")

def get_bookings_list(request):
    halls = Hall.objects.all()
    apartments = Apartment.objects.all()

    context = {
        "halls": halls,
        "apartments": apartments,
        # Include other context variables as needed
    }
    return render(request, "venue/bookings_list.html", context)

def add_bookings(request):
	return render(request, "venue/add_bookings_list.html",)




