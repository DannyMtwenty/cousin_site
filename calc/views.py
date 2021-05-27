from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):  #receives request
  #  return HttpResponse("Hello world") #returns httpresponse
  return render(request,'home.html',{'name':'Danny Wanyoike'})

def add(request):  #receives request
  val1=int(request.POST["num1"])
  val2=int(request.POST["num2"])
  res=val1+val2
  return render(request,'results.html',{'result':res})