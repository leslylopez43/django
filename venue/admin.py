from django.contrib import admin
from .models import Hall, Apartment, Tenant, Tenancy, Accommodation, Accommodation, Payment, BusinessOwner


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('accommodation_id', 'weddings', 'birthdays', 'parties', 'baby_shower', 'corporate_events', 'christmas', 'lifestyle_photoshot')

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('accommodation_id', 'check_in', 'check_out', 'guests', 'rooms', 'apartment_availability')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'first_name', 'last_name', 'email', 'mobile_phone')

@admin.register(Tenancy)
class TenancyAdmin(admin.ModelAdmin):
    list_display = ('accommodation_id', 'tenant', 'check_in', 'check_out', 'sleeps', 'venue_type')

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'accommodation_id')
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'full_name', 'email', 'pay_with', 'order_total')

@admin.register(BusinessOwner)
class BusinessOwnerAdmin(admin.ModelAdmin):
    list_display = ('accommodation_id', 'name', 'business_name', 'email', 'vat')
    
