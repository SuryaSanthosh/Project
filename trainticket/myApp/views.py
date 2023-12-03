from django.shortcuts import render,redirect,HttpResponse
from .models import User 
from .models import UserProfile  # Import the UserProfileForm from your app's forms.py
from .forms import UserProfileForm
from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib import messages


def index(request):

    return render(request,'index.html')
def user_index(request):

    return render(request,'user_index.html')





# Create your views here.


def register(request):
   if request.method=="POST":
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            confirm_password=request.POST['confirm-password']
            if password!=confirm_password:
                    messages.warning(request,"password is not matching")
                    return render(request,'signup.html')
            try:
                      if User.objects.get(username=username):
                             messages.warning(request,"Username is already taken")
                             return render(request,'register.html')
            except Exception as identifiers:
                      pass
            print(first_name,last_name,username,email,password)
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,role='USER')
              #make the user inactive  user.is_active=False
            user.save()
            return redirect('login')
   return render(request,'register.html')


def login(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        
        # Use the model class to query the database
        user = authenticate(request,username=username, password=password)
        
        if user is not None:
            auth_login(request,user)
            request.session['username']=username
            if user.role=='USER':
               messages.success(request,"Login Success!!!")
               return redirect('user_list')
            
            elif user.role=='ADMIN':
               return redirect('/dashboard/')
        else:
            messages.error(request,"Some thing went wrong")
            return redirect('login')
    response=render(request,'login.html')
    response['Cache-Control'] = 'no-store,must-revalidate'
    return response

def user_list(request):
      

       # Fetch a list of users from the database
    #users = User.objects.all()

    # You can perform additional logic here if needed

    # Render the user_list template and pass the users as context
    #return render(request, 'user_list.html', {'users': users})
    if "username" in request.session:
          response = render(request,'user_list.html')
          response['Cache-Control'] = 'no-store,must-revalidate'
          return response
    else:
          return redirect('login')
    


def handlelogout(request):
      if request.user.is_authenticated:
            logout(request)
      return redirect("login")




def edit_profile(request):
    if request.method == 'POST':
        # Get updated data from the form
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']

        # Update the user's profile with the new data
        user = request.user
        user.username = first_name
        user.last_name = last_name
        user.email = email

        user.save()

        messages.success(request, 'Profile updated successfully')
        return redirect('myprofile')

    return render(request, 'edit_profile.html', {'user': request.user})



def sbooktrain(request):

    return render(request,'sbooktrain.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
def userview(request):
    role_filter = request.GET.get('role')
    users = User.objects.filter(~Q(is_superuser=True))  # Exclude superusers by default

    if role_filter:
        users = users.filter(role=role_filter)

    #context = {'User_profiles': users, 'role_filter': role_filter}
    #return render(request, 'userview.html',context)

    page = request.GET.get('page', 1)
    paginator = Paginator(users, 10)  # Change 10 to the number of users per page you want
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'User_profiles': users, 'role_filter': role_filter}
    return render(request, 'userview.html', context)



from django.db.models import Q

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags




  
def activate_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    subject = 'Account Activation'
    html_message = render_to_string('activation_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = 'suryas2024b@gmail.com'
    recipient_list = [user.email]
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    return redirect('userview')

def deactivate_user(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_superuser:
        return HttpResponse("You cannot deactivate the admin.")
    user.is_active = False
    user.save()
    subject = 'Account Deactivation'
    html_message = render_to_string('deactivation_email.html', {'user': user})
    plain_message = strip_tags(html_message)
    from_email = 'suryas2024b@gmail.com'
    recipient_list = [user.email]
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
    # Send an email to the user here
    return redirect('userview')




from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required

@login_required
def submit_feedback(request):
    if request.method == "POST":
        feedback_message = request.POST.get('feedback_message')
        if feedback_message:
            Feedback.objects.create(user=request.user, message=feedback_message)
            # You can add additional logic here (e.g., sending a confirmation email)
            return redirect('feedback_thankyou')

    return render(request, 'feedback_form.html')




def feedback_thankyou(request):
     return render(request,'feedback_thankyou.html')


from django.shortcuts import render
from .models import Feedback

def adminfeedback(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'adminfeedback.html', {'feedback_list': feedback_list})




from .forms import TrainForm

def dashboard(request):
    # You can add logic here to retrieve data for the dashboard
    context = {
        'title': 'Admin Dashboard',
        'welcome_message': 'Welcome to the Admin Dashboard. Manage your system here.',
    }
    return render(request, 'dashboard.html', context)









from django.shortcuts import render, redirect
from .models import Train
from django.contrib import messages

def add_train(request):
    if request.method == 'POST':
        train_name = request.POST['train_name']
        train_number = request.POST['train_number']
        departure_station = request.POST['departure_station']
        departure_time = request.POST['departure_time']
        arrival_station = request.POST['arrival_station']
        arrival_time = request.POST['arrival_time']
        duration = request.POST['duration']
        #available_classes = request.POST.getlist('available_classes')

        # Create a new Train object and save it to the database
        train = Train(
            train_name=train_name,
            train_number=train_number,
            departure_station=departure_station,
            departure_time=departure_time,
            arrival_station=arrival_station,
            arrival_time=arrival_time,
            duration=duration,
            #available_classes=available_classes
        )
        train.save()

        messages.success(request, 'Train added successfully')  # Display a success message
        return redirect('trainview')  # Redirect to the add_train page to add more trains

    return render(request, 'addtrain.html')



from .models import Train
def trainview(request):
    trains = Train.objects.all()  # Retrieve all available trains from the database
    context = {'trains': trains}
    return render(request, 'trainview.html', context)





from .models import Station

def station_list(request):
    stations = Station.objects.all()
    return render(request, 'station_list.html', {'stations': stations})
from django.shortcuts import render, redirect
from .forms import StationForm

def add_station(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('station_list.html')  # Redirect to station list view
    else:
        form = StationForm()
    return render(request, 'add_station.html', {'form': form})




def myprofile(request):
    return render(request, 'myprofile.html')


# views.py
from django.shortcuts import render, redirect
from .models import Route, RouteDetails
from .forms import RouteForm
def add_route(request):
    if request.method == 'POST':
        destination_station = request.POST['destination_station']
        arrival_station = request.POST['arrival_station']
        route_stations = request.POST('route_stations','')
        departure_time = request.POST['departure_time']
        fare_amounts = request.POST.getlist('fare_amounts[]')

        # Create Route instance
        route = Route.objects.create(
            destination_station=destination_station,
            arrival_station=arrival_station,
            route_stations=route_stations,
            departure_time=departure_time,
            fare_amounts=fare_amounts
        )

        # Create RouteDetails instances
        for station, fare in zip(request.POST.getlist('station_name[]'), fare_amounts):
            RouteDetails.objects.create(route=route, station_name=station, fare_amount=fare)

        return redirect('display_routes')

    return render(request, 'add_route.html')

# views.py
from django.shortcuts import render
from .models import Route

def display_route(request):
    # Replace the following lines with your actual data retrieval logic
    departure_time = "Your Departure Time"
    destination_station = "Your Destination Station"
    route_stations = ["Station1", "Station2", "Station3"]
    departure_times = ["Time1", "Time2", "Time3"]
    fare_amounts = ["Fare1", "Fare2", "Fare3"]
    arrival_station = "Your Arrival Station"
    total_fare = "Your Total Fare"

    context = {
        'departure_time': departure_time,
        'destination_station': destination_station,
        'route_stations': route_stations,
        'departure_times': departure_times,
        'fare_amounts': fare_amounts,
        'arrival_station': arrival_station,
        'total_fare': total_fare,
    }

    return render(request, 'display_route.html', context)




# myApp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Train

def train_search(request):
    if request.method == 'POST':
        origin = request.POST.get('origin', '')
        destination = request.POST.get('destination', '')
        date = request.POST.get('date', '')

        # Perform your search logic here based on the criteria
        # For simplicity, let's assume we filter by origin and destination
        trains = Train.objects.filter(origin__icontains=origin, destination__icontains=destination)

        # Convert train objects to a list of dictionaries for JSON response
        train_list = [
            {
                'name': train.name,
                'origin': train.origin,
                'destination': train.destination,
                'departureTime': train.departure_time.strftime('%H:%M'),
                'arrivalTime': train.arrival_time.strftime('%H:%M'),
            }
            for train in trains
        ]

        return JsonResponse({'trains': train_list})

    return render(request, 'train_search.html')




# views.py
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from .models import Route

def search_train(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        departure_station = request.POST.get('departure_station')
        arrival_station = request.POST.get('arrival_station')

        try:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            # Filter routes based on the selected date, departure station, and arrival station
            routes = Route.objects.filter(
                Q(departure_station__icontains=departure_station) &
                Q(arrival_station__icontains=arrival_station) &
                Q(departure_time__date=selected_date)
            )
        except ValueError:
            # Handle invalid date format
            routes = Route.objects.all()
    else:
        routes = Route.objects.all()

    return render(request, 'search_train.html', {'routes': routes})





