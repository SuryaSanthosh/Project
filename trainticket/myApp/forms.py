from django import forms
from django.forms.models import inlineformset_factory
from .models import Trains, Route, Station, Seat  # Import other necessary models

class TrainForm(forms.ModelForm):
    class Meta:
        model = Trains
        fields = ['train_id', 'train_name', 'departure_station', 'departure_time', 'operating_days', 'train_type']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['arrival_station', 'arrival_time']

# Define RouteFormSet using inlineformset_factory
RouteFormSet = inlineformset_factory(Trains, Route, form=RouteForm, extra=1)

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'location']

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)

class SeatSelectionForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['seat_number', 'class_type']

from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Replace with your user profile model
        fields = [ 'phone', 'profile_photo','user']

