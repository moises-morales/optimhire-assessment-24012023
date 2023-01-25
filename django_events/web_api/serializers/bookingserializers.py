from events_manager.models import Booking
from rest_framework import serializers


class BookingCreateSerializer(serializers.HyperlinkedModelSerializer):

    event_id = serializers.IntegerField()
    customer_id = serializers.IntegerField()

    class Meta:
        model = Booking
        fields = ['event_id', 'customer_id']


class BookingRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['event', 'customer']
