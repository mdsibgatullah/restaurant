from typing import Any
from django.shortcuts import render

from django.views.generic.base import TemplateView

from restaurantapp.models import AboutUs, DeliciousMenu, Dishes, Slider

class Index(TemplateView):
    template_name = 'restaurantapp/index.html'


    # sanacks = DeliciousMenu.objects.filter(type="Sanacks")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().first()
        context['about'] = AboutUs.objects.all().first()
        context['dishes'] = Dishes.objects.all()
        context['spcial_dishes'] = Dishes.objects.filter(is_spcial=True)[0]
        return context

    # def post(self,request,*args,**kwargs):
    #     name = request.POST['contact_name']
    #     name = request.POST['contact_email']
    #     name = request.POST['contact_phone']
    #     name = request.POST['noofpeople']
        