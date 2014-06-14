from django.shortcuts import render

# Create your views here.

def licensing(request):
    return render(request, "licensing/licensing.html")