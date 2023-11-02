from django.db import models

# Create your models here.
class Contact(models.Model):
    person_number =[
        ("a",'1'),
        ("b",'2'),
        ("c",'3'),
        ("d",'4'),
        ("e",'5'),
        ("f",'6'),
        ("g",'7')
    ]
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=255)
    person = models.CharField(max_length=50,choices=person_number,default='1')
