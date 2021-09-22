from django.db import models

# Create your models here.
class Destination(models.Model):
     
    name = models.CharField(max_length=60)
    img = models.ImageField(default='/media/pics/mumbai.jpg',upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False) 