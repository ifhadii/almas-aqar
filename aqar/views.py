from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "pages/home.html")

def Contact_Us (request):
    return render(request, "pages/Contact_Us.html")

def Property_Owners (request):  
    return render(request, "pages/Property_Owners.html")

def Request_Electronic_Contract (request):
    return render(request, "pages/Request_Electronic_Contract.html")

def about_us (request):
    return render(request, "pages/about_us.html")
