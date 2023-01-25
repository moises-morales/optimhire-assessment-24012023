from django.db import models
from .baseModel import BaseModel
from .event import Event
from .customer import Customer

MAX_BOOKING_PER_CUSTOMER = 1


class Booking(BaseModel):

    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, related_name='bookings', on_delete=models.PROTECT)

    
    def __str__(self) -> str:
        return f"Booking for {self.id}: {self.event.name} - {self.customer.first_name} {self.customer.last_name} - {self.customer.email} "

    @classmethod
    def is_available_space(self, event):
        return Booking.objects.filter(event=event).count() < event.room.capacity

    @classmethod
    def already_has_booking_for_the_event(self, event, customer):
        return Booking.objects.filter(event=event, customer=customer).count() >= MAX_BOOKING_PER_CUSTOMER


    @classmethod
    def get_objects(self, event_id, customer_id):
        try:
            event = Event.objects.filter(id=event_id).first()
            customer = Customer.objects.filter(id=customer_id).first()
            return (event, customer)
        except:
            return None

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
