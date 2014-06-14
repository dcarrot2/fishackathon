from django.shortcuts import render

# Create your views here.

#def index(request):
#return render(request, "registration/base.html")


def index(request):
    return render(request, "reporting/check.html")

def registration(request):
    return render(request, "registration/register.html")