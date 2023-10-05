from django.shortcuts import render,redirect,HttpResponse
from .models import User 

from django.contrib.auth import authenticate ,login as auth_login,logout
from django.contrib import messages

def index(request):

    return render(request,'index.html')



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
               messages.success(request,"Login Success!!!")
               return HttpResponse("Admin login ")
                          
        else:
            messages.error(request,"Some thing went wrong")
            return redirect('user_list')
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