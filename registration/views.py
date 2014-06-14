from django.shortcuts import render
from registration.models import Manager
# Create your views here.


responses ={}

def index(request):
    return render(request, "registration/base.html")

def registrationA(request):
    
    return render(request, "registration/register.html", {'section': "A"})

def registrationB(request):
    
    return render(request, "registration/register.html", {'section':  "B"})


def session(request):
    sessionID = request.COOKIES['sessionid']
    section = request.POST['section']
    print 'Section: ', section
    try:
        global responses
        if (sessionID not in responses.keys()):
            print "creating a new key"
            responses[sessionID] = []
        for i in range(0,10):
            print request.POST["choice" + str(i+1)]
            #responses[sessionID].append()
        print "Responses", responses
        
    except(KeyError):
        print("Check try statement")
        return render(request, 'registration/register/html'), {'error_message': "You forgot to answer one or more questions"}
    
    if(section=="A"):
        following_section = "B"
