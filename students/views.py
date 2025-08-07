from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<p style='color:red;'>This is the index page of student.</p>")

def about(request):
    return HttpResponse("<p style='color:red;'>Hello, world! This is the about page of student.</p>")

def contact(request):
    return HttpResponse("<p style='color:red;'>This is the contact page of student.</p>")

def even_odd(request):
    a=11
    if a%2==0:
        return HttpResponse("This is an even number")
    else:       
        return HttpResponse("This is an odd number")
    
def file(request):
    a="Django Python Course update"
    b= ["Abhinav", "Abhishek", "Amit", "Ankit", "Anshika"]
    return render(request, "index.html", {"data": a, "names": b})


