from django.shortcuts import render
from .models import Member
# Create your views here.
def index(request):  #receives request
   
  members=Member.objects.all()

  return render(request,'index.html',{'members':members})