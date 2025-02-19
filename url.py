from django.urls   import path
from . import views

urlpatterns = [
    path('home/',  views.home,  name='home'),
    path('login/', views.login_view, name="login"),
    path(r'^departments/', views.get_departments, name="departments"),
    # path(r'^school/', views.get_SCHOOL, name="School")
    
    
    
           ]