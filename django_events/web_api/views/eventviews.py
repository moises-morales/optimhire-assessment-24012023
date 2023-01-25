from events_manager.models import Event

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from web_api.serializers import EventCreateSerializer, EventRetrieveSerializer

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

import datetime


class EventListCreateAPIView(ListCreateAPIView):
    """
    API endpoint that allows create-list the events
    """
    logger = logging.getLogger(__name__)

    queryset = Event.objects.filter(public=True).all()
    serializer_class = EventCreateSerializer

    def create(self, request, *args, **kwargs):
        self.logger.info(f"request.data: {request.data}")
        other_events = Event.objects.filter(date=request.data['date'], room__id=request.data['room_id'])
        self.logger.info(f"other_events: {other_events}")
        
        if datetime.datetime.strptime(request.data['date'], "%Y-%m-%d") < datetime.datetime.today():
            return Response("You cannot create an event with a previous date", status=status.HTTP_403_FORBIDDEN)
        elif other_events.count() > 0:
            return Response("You cannot have many events in the same room on the same day", status=status.HTTP_403_FORBIDDEN)
        else:
            return super().create(request, *args, **kwargs)

    def get(self, request, format=None):
        self.logger.info("Getting the public events")
        events = self.get_queryset()
        serializer = EventRetrieveSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)
