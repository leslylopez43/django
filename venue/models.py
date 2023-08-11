from django.db import models

# Create your models here.

class Hall(models.Model):
    accommodation_id = models.AutoField(primary_key=True)
    weddings = models.BooleanField(default=False)
    birthdays = models.BooleanField(default=False)
    parties = models.BooleanField(default=False)
    baby_shower = models.BooleanField(default=False)
    corporate_events = models.BooleanField(default=False)
    christmas = models.BooleanField(default=False)
    lifestyle_photoshot = models.BooleanField(default=False)

class Apartment(models.Model):
    accommodation_id = models.AutoField(primary_key=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    guests = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    apartment_availability = models.CharField(max_length=20, choices=[("available", "Available"), ("unavailable", "Unavailable")])

class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    plus_18s = models.PositiveIntegerField()
    under_18s = models.PositiveIntegerField()
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=200)

class Tenancy(models.Model):
    accommodation_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    sleeps = models.PositiveIntegerField()
    venue_type = models.CharField(max_length=100)

class Accommodation(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    accommodation_id = models.AutoField(primary_key=True)

class Payment(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200)
    post_code = models.CharField(max_length=20)
    email = models.EmailField()
    contact_details = models.CharField(max_length=100)
    billing_address = models.CharField(max_length=200)
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ]
    pay_with = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    add_new_card = models.BooleanField(default=False)
    donate_to_charity = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)

class BusinessOwner(models.Model):
    accommodation_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    vat = models.CharField(max_length=20)

    