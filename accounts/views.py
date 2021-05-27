from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth   #imports user model and auth for login
# Create your views here.
def register(request):  #receives request
  if request.method =='POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name'] 
    user_name=request.POST['user_name'] 
    password1=request.POST['password1'] 
    password2=request.POST['password2'] 
    email=request.POST['email'] 
    if password1==password2:   
      if User.objects.filter(username=user_name).exists():
        print("username taken")  
      elif User.objects.filter(email=email).exists():
        print("email taken")
      else:
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,password=password1,email=email)
        user.save()
        print("user created")
        return redirect('/')
      
    else:   
        print("Password mismatch") 

    return render(request,'registration/register.html')
  

def login(request):  #receives request 
  return render(request,'registration/login.html')