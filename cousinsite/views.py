from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):  #receives request

  members=Member.objects.all()
  photos = Photo.objects.all()

  return render(request,'index.html',{'members':members,'photo':photos})


def register(request):  # receives request
  if request.method=='POST':
    first_name=request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email= request.POST['email']
    if password1 == password2:
      if User.objects.filter(username=username).exists():

        messages.error(request, 'username taken!')
      elif User.objects.filter(email=email).exists():

        messages.error(request, 'email taken!')
      else:
        user = User.objects.create_user(  first_name=first_name, last_name=last_name, username=username, password=password1,
                                        email=email)
        user.save()
        messages.success(request, 'You registered successfully!')
    else:

      messages.error(request, 'password mismatch!')

  return render(request, 'registration/register.html')


def admin_view(request):
    return render(request, 'dashboards/admin.html')

def chairperson_view(request):

    return render(request, 'dashboards/chairperson.html')

def login(request):  # receives request
  if request.method=='POST':
    username=request.POST['username']
    password= request.POST['password']

    user=auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      print('user exists')
      messages.success(request, 'Login successiful')
      return  redirect('chairperson')
    else:
      messages.error(request, 'invalid username or password')
      return redirect('login')

  else:
    return render(request, 'registration/login.html')


def logout(request):  # receives request
  auth.logout(request)
  return redirect('/')

def gallery(request):
  categories = Category.objects.all()
  photos=Photo.objects.all()
  context = {'categories': categories,'photos': photos}
  return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
  photo=Photo.objects.get(id=pk)

  return render(request, 'photos/photo.html', {'photo':photo})


def addPhoto(request):
  categories = Category.objects.all()

  if request.method == 'POST':
    data = request.POST
    images = request.FILES.getlist('images')

    if data['category'] != 'none':
      category = Category.objects.get(id=data['category'])
    elif data['category_new'] != '':
      category, created = Category.objects.get_or_create(
        name=data['category_new'])
    else:
      category = None

    for image in images:
      photo = Photo.objects.create(
        category=category,
        description=data['description'],
        image=image,
      )

    return redirect('gallery')
  context = {'categories': categories}
  return render(request, 'photos/add.html', context)

