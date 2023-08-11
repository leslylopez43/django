from django import forms
from django import forms

class BookingsAvailabilityForm(forms.Form):
    hall_accommodation_id = forms.CharField(label='Accommodation ID', required=True)
    weddings = forms.BooleanField(label='Weddings', required=False)
    birthdays = forms.BooleanField(label='Birthdays', required=False)
    # ... Define other fields for hall availability here

    apartment_accommodation_id = forms.CharField(label='Accommodation ID', required=True)
    check_in = forms.DateTimeField(label='Check-in', required=True)
    check_out = forms.DateTimeField(label='Check-out', required=True)
    guests = forms.IntegerField(label='Guests', required=True)
    rooms = forms.IntegerField(label='Rooms', required=True)
    apartment_availability = forms.ChoiceField(label='Apartment Availability', choices=[('available', 'Available'), ('unavailable', 'Unavailable')], required=True)
