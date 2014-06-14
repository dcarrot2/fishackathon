from django.shortcuts import render

# Create your views here.
def reporting(request):
    return render(request,"reporting/reporting.html")