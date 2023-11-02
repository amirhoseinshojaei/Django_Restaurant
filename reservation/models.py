from django.db import models

# Create your models here.
class Reservation(models.Model):
    person_number =[
        ("a",'1'),
        ("b",'2'),
        ("c",'3'),
        ("d",'4'),
        ("e",'5'),
        ("f",'6'),
        ("g",'7')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    number = models.IntegerField()
    date = models.DateField(auto_now=False,auto_now_add=True)
    time = models.TimeField(auto_now=False,auto_now_add=True)
    person = models.CharField(max_length=255,choices=person_number,default='1')

    def __str__(self):
        return "{},{}".format(self.name,self.date)