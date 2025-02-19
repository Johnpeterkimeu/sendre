from datetime import date
import datetime
import json
from multiprocessing import Value
import os
#from typing import Self
from django.shortcuts import render,redirect
from django.conf.locale.en.formats import SHORT_DATETIME_FORMAT
from django.  http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from psycopg2 import Date

import staff
# from wsgiref.types import FileWrapper
#from setuptools import _BuildInfo
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')
def page(request):
    staffdata=StaffMovement.objects.all()
    print("===========================")
       
    return render(request,'review.html',{ 'staffdata' : staffdata})
# def Application_details(request):
#     staffdata=StaffMovement.objects.all()
#     print("===========================")
       
#     return render(request,'review.html',{ 'staffdata' : staffdata})
def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Username not found')
            return redirect('/login/')

        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid password')
          
        else:
                login(request, user)
                return redirect('/login/')
        return render(request, 'login.html')

  
   

def register(request):

    if request.method == 'POST':
        Firstname = request.POST.get('Firstname')
        lastname =request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        PASSWORD =request.POST.get('Confirm Password')


        if   User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists')
            return redirect('/register/')

        if password != PASSWORD:
            messages.info(request, 'password not matching')
            return redirect('/register/')
        else:
            user = User.objects.create_user(
                first_name=Firstname,
                last_name=lastname,
                username=username
            )
            user.set_password(password)
            user.save()

            messages.success(request, 'user created successfully')
            return redirect('/login/')

    return render(request, 'login.html')
def movement(request):
    if request.method=='POST':
       Date_Reported= request.POST.get("Date reported on 1st Appointment")
       Current =request.POST.get("Current department")
       To= request.POST.get("Department to")
       LastDate=request.POST.get("The Last Date of service  from the current department")
       Absent = request.POST.get("option")
       
       DATE_CHOSEN =request.POST.get("ABSENT FROM DUTY")
       Evidence = request.POST.get("upload")
       RESUMED = request.POST.get("resumed")
       
       Returned= request.POST.get("date_resumed")
       
       
       
       print("=========================", Date_Reported);
       exit
       
       staff_movement = StaffMovement(
         date_reported=Date_Reported,
           current=Current,
           To=To,
           last_date=LastDate,
           Absent=Absent,
          
            date_chosen=DATE_CHOSEN,
           Evidence=Evidence,
            resumed=RESUMED,
             
             returned=Returned,
            
       )
       
    #    StaffMovement.objects.get('Current department')
    #    return render(request,'movement.html')
       print(staff_movement)
       exit
       
       staff_movement.save()
       
    #    return redirect('page')
    
    return render(request, 'movement.html')
   

    print('success')
    exit
    
        

def get_departments(request):
   
    if request.is_ajax() and request.method == "GET":
        # Retrieve data from the database based on parameters or query strings
        query = request.GET.get("term", "")
        departments = Departments.objects.filter(Department_name__icontains=query)
        results = []
        for dept in departments:
            place_json =dept.Department_name
            results.append(place_json)
        print(results)
        return JsonResponse(results, safe=False)
    

def get_SCHOOL(request):
       if request.is_ajax() and request.method == "GET":
            # Retrieve data from the database based on parameters or query strings
            query = request.GET.get("term", "")
            schools = School.objects.filter(School_name__icontains=query)
            results = []
            for sch in schools:
                place_json =sch.School_name
                results.append(place_json)
            print(results)
            return JsonResponse(results, safe=False)
        
    