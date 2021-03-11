from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#use one to one extend

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)	 
    cell_phone_number = models.CharField(max_length = 30,null = True,blank = True,default="")	   
    points = models.IntegerField(default = 0)    
    

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()	
