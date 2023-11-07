from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # Replace with your user profile model
        fields = [ 'phone', 'profile_photo','user']



from .models import Train

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'




from django import forms
from .models import Station

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['station_name', 'code']
