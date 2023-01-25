# Django
from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from events_manager.models import Booking
from .factories import CustomerFactory, EventFactory


class BookingTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.event = EventFactory.create()
        self.customer = CustomerFactory.create()


    def test_create_booking_happy_path(self):
        data = {"event_id":self.event.id, "customer_id":self.customer.id}
        response = self.client.post(
            '/api/booking/', 
            data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_twice_same_event_same_customer(self):
        data = {"event_id":self.event.id, "customer_id":self.customer.id}
        response = self.client.post(
            '/api/booking/', 
            data,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            '/api/booking/', 
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content.decode('ascii'), '"The customer already has a booking for the event."')

    def test_create_booking_wrong_data(self):
        data = {"event_id":100000, "customer_id":2000}
        response = self.client.post(
            '/api/booking/', 
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.content.decode('ascii'), '"The customer and/or the event don not exist!"')

    def test_create_booking_private_event(self):
        self.event.public = False
        self.event.save()

        data = {"event_id":self.event.id, "customer_id":self.customer.id}
        response = self.client.post(
            '/api/booking/', 
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)
        self.assertEqual(response.content.decode('ascii'), '"The event is private, you can not book an space!"')

    def test_cancel_booking(self):
        data = {"event_id":self.event.id, "customer_id":self.customer.id}
        response = self.client.post(
            '/api/booking/', 
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.delete(
            f"/api/booking/{self.event.id}/{self.customer.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

