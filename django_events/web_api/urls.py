from django.urls import path
from web_api.views import (RoomCreateAPIView, RoomDestroyedAPIView, EventListCreateAPIView, 
                          BookingCreateAPIView, BookingDestroyedAPIView)

app_name = "web_api"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('room/', RoomCreateAPIView.as_view(), name="Create Room - API"),
    path('room/<int:pk>/', RoomDestroyedAPIView.as_view(), name="Delete Room - API"),
    path('event/', EventListCreateAPIView.as_view(), name="Create Event - API"),
    path('booking/', BookingCreateAPIView.as_view(), name="Create Booking - API"),
    path('booking/<int:pk>/<int:customer_id>/', BookingDestroyedAPIView.as_view(), name="Delete Booking - API"),
]
