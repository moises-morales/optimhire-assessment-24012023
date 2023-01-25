from events_manager.models import Room

from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from web_api.serializers import RoomCreateSerializer, RoomRetrieveSerializer

import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class RoomCreateAPIView(CreateAPIView):
    """
    API endpoint that allows create rooms
    """
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer


class RoomDestroyedAPIView(DestroyAPIView):
    """
    API endpoint that allows destroy rooms
    """
    logger = logging.getLogger(__name__)

    serializer_class = RoomRetrieveSerializer

    def get_queryset(self):
        queryset = Room.objects.filter(id=self.kwargs['pk'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.logger.info(f"Object to delete: {instance}")
        events = instance.events.all()
        self.logger.info(f"Events related to the event to delete: {events}")
        if instance.events.all().count() > 0:
            return Response("Cannot delete the event because it has events", status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
