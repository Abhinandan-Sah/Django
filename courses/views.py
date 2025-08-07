from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# from courses.views import CourseListView, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView
# Create your views here.


def CourseListView(request):
    return HttpResponse('This is the course list view')

def CourseDetailView(request, courseName):
    return HttpResponse(f'This is the detail view for course {courseName}')

def CourseCreateView(request):
    return HttpResponse('This is the create view for course')

def CourseUpdateView(request, pk):
    return HttpResponse(f'This is the update view for course with id {pk}')

def CourseDeleteView(request, pk):
    return HttpResponse(f'This is the delete view for course with id {pk}')

def jsondata(request):
    data = {
        'name': 'Abhinav',
        'age': 20,
        'city': 'Delhi'
    }
    return JsonResponse(data)

def datavalue(request, name, age):
    return HttpResponse(f'This is the data value view for {name} <br> who is {age} years old')