from django.contrib import admin
from .models import Departments, School, StaffMovement
from django.urls import path
from . import views
from .views import movement
#Register your models here.

admin.site.register(StaffMovement),
admin.site.register(Departments),
admin.site.register(School)

urlpatterns = [
     path('', views.home, name="home"),
      path('movement/', movement ,name='movement'),
 ]