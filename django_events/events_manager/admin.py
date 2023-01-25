from django.contrib import admin
from .models import Booking, Company, Customer, Event, Room


# Register your models here.

admin.site.register(Booking)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(Room)
