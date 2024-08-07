from django.urls import path
from customadmin.views import Index, BookingView

urlpatterns = [
    path('',Index.as_view(), name='custom-admin'),
    path('booking',BookingView.as_view(), name='booking')
]
