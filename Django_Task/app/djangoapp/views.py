from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from pymongo import MongoClient
from django.db import connection
client = MongoClient("localhost")
db = client["data"]
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("User authenticated successfully")
            return redirect('players_view')
        else:
            messages.error(request, "Invalid username or password.")
            print("User authentication failed")
            return redirect('login_view')
    return render(request,"login.html")

def logout_view(request):
    return render(request,"logout.html",{})

def home(request):
    return render(request,"Home.html",{})

def registration_student_view(request):
    return render(request,"Registration.html",{})

def details_view(request):
    return render(request,"student_details.html",{})
