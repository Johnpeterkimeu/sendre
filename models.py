import datetime
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.timezone import now
# Create your models here.


class StaffMovement(models.Model):
      
      date_reported = models.DateTimeField(default=now())

      current = models.CharField(max_length=30 ,default='')
      To = models.CharField(max_length=30, default='')
      last_date  = models.DateTimeField(default=now())

      Absent = models.TextField(default='')
      date_chosen = models.DateTimeField(default=now())
      
      Evidence = models.FileField(upload_to="uploads/")
      resumed = models.TextField(default='')
      returned = models.DateTimeField(default=now())
     
      Status =models.TextField(default='')
      Comments = models.TextField(default='')
    
class Departments(models.Model):
      Department_code= models.CharField(max_length=8)
      Department_name= models.CharField(max_length=80)
class School(models.Model):
      School_code= models.CharField(max_length=9)
      School_name= models.CharField(max_length=80)
# class CustomDateInput(forms.DateInput):
#       input_type="date"
      
      
#       def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.attrs.update({"onfocus": "disableDates(this)"})
      
      
# class staffMovementForm(forms.ModelForm):
#       my_date=forms.DateField(widget=CustomDateInput())
#     class Meta:
#         model = staffMovement
#         fields = [
            
#             'Date_reported',
#             'Current',
          
#             'To',
           
#             'LastDate',
#             'ABSENT',
#             'CHOSEN',
#             'Evidence',
#             'Resumed',
#             'Returned'
          
#         ]
        
#     def clean(self):
#         cleaned_data = super().clean()
#         required_fields = ['current_department', 'Department_to', 'Specify']
#         for field in required_fields:
#             value = cleaned_data.get(field)
#             if value is None:
#                 raise forms.ValidationError(f'{field} is required.')
#             if isinstance(value, str) and value.strip() == '':
#                 raise forms.ValidationError(f'{field} cannot be empty.')
#         return cleaned_data

     
       
       
       