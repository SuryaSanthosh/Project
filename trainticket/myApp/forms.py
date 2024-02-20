from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Replace with your user profile model
        fields = [ 'phone', 'profile_photo','user']



from .models import Train
from django import forms
from django.forms import inlineformset_factory
from .models import Train, Route

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['train_id', 'train_name', 'departure_station', 'departure_time']



# forms.py
# forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Train, Route

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['train_id', 'train_name', 'departure_station', 'departure_time']

# myApp/forms.py

from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['arrival_station', 'arrival_time']  # Correct fields to match the Route model

RouteFormSet = inlineformset_factory(Train, Route, form=RouteForm, extra=1)


from django import forms
from .models import Station 
class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'location']

# If you need a form for capturing payment-related data,
# you can create a form like this:

from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)

# forms.py

from django import forms
from .models import Seat

class SeatSelectionForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['seat_number', 'class_type']
