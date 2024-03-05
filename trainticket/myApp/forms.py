

from django import forms
from django.forms.models import inlineformset_factory
from .models import Trains, Route, Station, Seat,Compartment # Import other necessary models

from django import forms

class AddTrainForm(forms.Form):
    train_id = forms.CharField(max_length=100)
    train_name = forms.CharField(max_length=100)
    departure_station = forms.CharField(max_length=100)
    departure_time = forms.TimeField()
    operating_days = forms.MultipleChoiceField(choices=[('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')])
    train_type = forms.ChoiceField(choices=[('express', 'Express'), ('local', 'Local'), ('high-speed', 'High-Speed'), ('seasonal', 'Seasonal')])
    number_of_seats = forms.IntegerField()

from django import forms
from django.forms import formset_factory

class RouteForm(forms.Form):
    arrival_station = forms.CharField(max_length=100)
    arrival_date = forms.DateField()
    arrival_time = forms.TimeField()

RouteFormSet = formset_factory(RouteForm, extra=1)

class CompartmentForm(forms.ModelForm):
    class Meta:
        model = Compartment
        fields = ['compartment_type', 'num_compartments', 'compartment_capacity']
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

from django import forms

class UserSearchForm(forms.Form):
    departure_station = forms.CharField(max_length=100)
    arrival_station = forms.CharField(max_length=100)
    departure_date = forms.DateField()
