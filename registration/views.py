from django.shortcuts import render
from registration.models import Manager, Canoe
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


responses ={}

def index(request):
    return render(request, "registration/base.html")

def registrationA(request):
    
    return render(request, "registration/register.html", {'section': "A"})

def registrationB(request):
     
    return render(request, "registration/register.html", {'section':  "B"})

@csrf_exempt
def session(request):
#     print request
    sessionID = request.COOKIES['sessionid']
    section = request.POST['section']
    print 'Section: ', section
    try:
        global responses
        if (sessionID not in responses.keys()):
            print "creating a new key"
            responses[sessionID] = []
        if(section =="A"):
            for i in range(0,8):
                print i
                print request.POST["choice" + str(i+1)]
                responses[sessionID].append(request.POST["choice" + str(i+1)])
                #responses[sessionID].append()
            print "Responses", responses
        else:
            for i in range (10,38):
                print i
                print request.POST["choice" + str(i)]
                responses[sessionID].append(request.POST["choice"+str(i)])
            print 'Responses', responses
    except(KeyError):
        print("Check try statement")
        return render(request, 'registration/register/html'), {'error_message': "You forgot to answer one or more questions"}
    
        
    if(section=="A"):
        following_section = "B"
        return render(request, "registration/register.html", {'section': following_section}) 
    else:
        for x in range(len(responses[sessionID])):
            responses[sessionID][x] = str(responses[sessionID][x])
            
        print "Responses: ", responses
        m = Manager(name_of_fisher=responses[sessionID][0], date_of_birth=responses[sessionID][1])

