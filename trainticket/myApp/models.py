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



from django.db import models
class Train(models.Model):
    train_name = models.CharField(max_length=100)
    train_number = models.CharField(max_length=10)
    departure_station = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_station = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    duration = models.CharField(max_length=20)
    available_classes = models.CharField(max_length=100)





from django.db import models

class Station(models.Model):
    station_name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.station_name
    


from django.db import models

class Route(models.Model):
    destination_station = models.CharField(max_length=255, default='')
    arrival_station = models.CharField(max_length=255)
    route_stations = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    fare_amounts = models.JSONField()

    def __str__(self):
        return f'{self.departure_station} to {self.arrival_station}'
class RouteDetails(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    station_name = models.CharField(max_length=255)
    fare_amount = models.PositiveIntegerField()







