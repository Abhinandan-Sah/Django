from django.shortcuts import render, HttpResponse

# Create your views here.
# Create your views here.
def index(request):
    return HttpResponse('This is the index path of teachers')

def about(request):
    return HttpResponse('This is the about path of teachers')

# Create your views here.
def contact(request):
    return HttpResponse('This is the contact path of teachers')