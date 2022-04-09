from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("hai")


def hello(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

