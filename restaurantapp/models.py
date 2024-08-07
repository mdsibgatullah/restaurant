from django.db import models
from solo.models import SingletonModel
# Create your models here.
class SliderItem(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slider/',default='slider/slider.jpeg')
    btn_one = models.URLField()
    btn_two = models.URLField()
    def __str__(self):
        return self.name
    
class AboutItem(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='slider/',default='slider/slider.jpeg')
    def __str__(self):
        return self.name
    
class Slider(SingletonModel):
    name = models.CharField(max_length=20)
    slider_item = models.ManyToManyField(SliderItem)

class AboutService(models.Model):
    # icon_class = models.CharField(max_length=20)
    image = models.ImageField(upload_to='icon')
    service_title = models.CharField(max_length=50)
    def __str__(self):
        return self.service_title

class AboutUs(SingletonModel):
    greating_text = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    about_item = models.ManyToManyField(AboutItem)
    about_service = models.ManyToManyField(AboutService)
    def __str__(self):
        return self.title
    
class Dishes(models.Model):
    title = models.CharField(max_length=20)
    offer = models.CharField(max_length=20)
    offer_price = models.FloatField()
    price = models.FloatField()
    description = models.CharField(max_length=150)
    btn = models.URLField()
    image_one = models.ImageField(upload_to='image_one',default='slider/slider.jpeg')
    image_two = models.ImageField(upload_to='image_two',default='slider/slider.jpeg')
    is_spcial= models.BooleanField(default=False)
    def __str__(self):
        return self.title

class DeliciousMenu(models.Model):
    TYPE_CHOICES = (
        ("Sanacks","Sanacks"),
        ("Desert","Desert"),
        ("Dinner","Dinner"),
        ("Freshfood","Freshfood"),
    )
    type = models.CharField(max_length=50,choices=TYPE_CHOICES)
    food_image = models.ImageField(upload_to="FoodImage",default="food.jpg")
    food_name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.food_name

class Booking(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    no_of_people = models.CharField(max_length=30)
    date = models.DateField()
    def __str__(self):
        return self.name



    
