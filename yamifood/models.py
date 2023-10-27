from django.db import models

# Create your models here.
class Food(models.Model):
    FOOD_TYPE = [
        ("l","Lunch",),
        ("d","Drinks",),
        ("d","Dinner",),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length= 100)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to= 'foods/')
    type = models.CharField(max_length=50,choices= FOOD_TYPE, default="Lunch")
    pub_date = models.DateTimeField(auto_now= False , auto_now_add=True)
    status = models.BooleanField(default= False)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    image_name = models.ImageField(upload_to='gallery/')
    date = models.DateTimeField(auto_now= False , auto_now_add= True)

    def __str__(self):
        return "{},{}".format(self.image_name,self.date)