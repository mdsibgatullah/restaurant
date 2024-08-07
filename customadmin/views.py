from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class Index(TemplateView):
    template_name = 'customadmin/index.html'

class BookingView(TemplateView):
    template_name = 'customadmin/booking.html'