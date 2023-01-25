from events_manager.models import Room
from rest_framework import serializers


class RoomCreateSerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.IntegerField()

    class Meta:
        model = Room
        fields = ['name', 'capacity', 'company_id']


class RoomRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ['name', 'capacity', 'company']
