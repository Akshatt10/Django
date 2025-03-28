from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def home(request):
    # return HttpResponse("Hello, Batman! This is the home page.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, Batman! This is the aboutt page.")


def contact(request):
    return HttpResponse("Hello, Batman! This is the contact page.")