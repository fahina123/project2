
from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),

    path("",views.hello,name="hello"),

     path("contact",views.contact,name="contact")
  
]