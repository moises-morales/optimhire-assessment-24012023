from events_manager.models import Event
from rest_framework import serializers


class EventCreateSerializer(serializers.HyperlinkedModelSerializer):

    room_id = serializers.IntegerField()
    company_id = serializers.IntegerField()


    class Meta:
        model = Event
        fields = ['name', 'date', 'public', 'room_id', 'company_id']


class EventRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['name', 'date', 'public', 'room', 'company']
