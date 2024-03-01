from django.db import models
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

from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone

class Route(models.Model):
    trains = models.ForeignKey('Trains', on_delete=models.CASCADE)
    arrival_station = models.CharField(max_length=100)
    arrival_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.arrival_station} - {self.arrival_time}"

from django.db import models

class Trains(models.Model):
    train_id = models.CharField(max_length=50, unique=True)    
    train_name = models.CharField(max_length=100)
    departure_station = models.CharField(max_length=100)
    departure_time = models.TimeField()
    operating_days = models.CharField(max_length=100)  
    train_type = models.CharField(max_length=50)

    def __str__(self):
        return self.train_name





from django.db import models

class RouteDetails(models.Model):
    # Define your fields here
    pass





class Payment(models.Model):
    order_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
from django.db import models

class Order(models.Model):
    # Define your fields here
    pass




from django.db import models

class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    class_type = models.CharField(max_length=20)

    def __str__(self):
        return self.seat_number


from django.db import models

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
