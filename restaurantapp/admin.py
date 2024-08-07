from django.contrib import admin

from solo.admin import SingletonModelAdmin

from restaurantapp.models import AboutItem, AboutUs, Booking, DeliciousMenu, Slider, SliderItem, AboutService, Dishes

# Register your models here.
admin.site.register(SliderItem)
admin.site.register(Slider,SingletonModelAdmin)
admin.site.register(AboutItem)
admin.site.register(AboutService)
admin.site.register(AboutUs,SingletonModelAdmin)
admin.site.register(Dishes)
admin.site.register(DeliciousMenu)
admin.site.register(Booking)