from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Batman! This is the home page.")


def about(request):
    return HttpResponse("Hello, Batman! This is the aboutt page.")


def contact(request):
    return HttpResponse("Hello, Batman! This is the contact page.")