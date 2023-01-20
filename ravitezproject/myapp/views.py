
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def loginfun(request):
    return render(request,"login.html")
def shopfun(request):
    return render(request,"shop.html")
def createaccountfun(request):
    return render(request,"createaccount.html")

        



