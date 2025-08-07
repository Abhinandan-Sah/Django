from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<p style='color:red;'>This is the index page.</p>")

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

def contact(request):
    return HttpResponse("This is the contact page.")