from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'ADMIN'
        USER="USER",'User'

    role = models.CharField(max_length=50,choices=Role.choices)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)


    def __str__(self):
        return self.user.username
    
    from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)









# models.py

from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone
class Train(models.Model):
    train_id = models.CharField(max_length=50)  # Add this line
    train_name = models.CharField(max_length=100)
    departure_station = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_station = models.CharField(max_length=100)
    arrival_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.train_name

class Route(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='routes')
    arrival_station = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Route for {self.train} to {self.arrival_station}"

# models.py

from django.db import models

class RouteDetails(models.Model):
    # Define your fields here
    pass


# If you need to store payment-related information in your database,
# you can create models for it. For example:

from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
