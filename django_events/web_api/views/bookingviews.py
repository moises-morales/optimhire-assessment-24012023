from events_manager.models import Booking

from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from web_api.serializers import BookingCreateSerializer, BookingRetrieveSerializer

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class BookingCreateAPIView(CreateAPIView):
    """
    API endpoint that allows create bookings
    """
    logger = logging.getLogger(__name__)
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer

    def post(self, request, *args, **kwargs):
        self.logger.info(f"request.data: {request.data}")
        event, customer = Booking.get_objects(request.data["event_id"], request.data["customer_id"])
        if event is None or customer is None:
            return Response("The customer and/or the event don not exist!", status=status.HTTP_404_NOT_FOUND)
        elif not event.public:
            return Response("The event is private, you can not book an space!", status=status.HTTP_406_NOT_ACCEPTABLE)
        elif not Booking.is_available_space(event):
            return Response("The event does not have spaces to booking anymore.", status=status.HTTP_400_BAD_REQUEST)
        elif Booking.already_has_booking_for_the_event(event, customer):
            return Response("The customer already has a booking for the event.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().post(request, *args, **kwargs)       


class BookingDestroyedAPIView(DestroyAPIView):
    """
    API endpoint that allows destroy rooms
    """
    logger = logging.getLogger(__name__)

    serializer_class = BookingRetrieveSerializer
    lookup_fields = ['event__id', 'customer__id']

    def get_queryset(self):
        self.logger.info(f"{self.kwargs}")
        queryset = Booking.objects.filter(customer__id=self.kwargs['customer_id'])
        return queryset
