from django.db import models

# Create your models here.
# company models to understand what is going 
class Company(models.Model):
    Company_name= models.CharField(max_length=100)
    Company_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    about= models.TextField()
    types = models.CharField(max_length=50,choices=
                             ( ('IT','Information Technology'),
                              ('Non It', 'Non-it'),
                              ('Finacal','finacal'),
                              ('Electrions','EE'),  
                             ))
    added_date= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# Employee Model 
