import factory
from factory.django import DjangoModelFactory
from events_manager.models import Booking, Event, Customer, Room, Company



class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company
    name =  factory.Faker('sentence', nb_words=3)


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    name = factory.Faker('sentence', nb_words=2)
    capacity = 2
    company = factory.SubFactory(CompanyFactory)


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = factory.Faker('sentence', nb_words=2)
    date = '2023-12-12'
    public = True
    room = factory.SubFactory(RoomFactory)
    company = factory.SubFactory(CompanyFactory)


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = "tester@testing.com"