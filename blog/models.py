from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length= 100)
    description = models.CharField(max_length=150)
    content = RichTextField()
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    date = models.DateField(auto_now=False,auto_now_add=True)
    time = models.TimeField(default= timezone.now)
    image = models.ImageField(upload_to='blogs/',null=True,blank=True)
    category = models.ForeignKey("Category",related_name= "categorys",null=True,blank=True,on_delete=models.CASCADE)
    tag = models.ManyToManyField("Tag",related_name="tags")

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=25)
    publish_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=25)
    publish_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey("Blog",related_name='comments',on_delete=models.CASCADE)
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email  = models.EmailField(max_length=255)
    message = RichTextField()

    def __str__(self):
        return self.email