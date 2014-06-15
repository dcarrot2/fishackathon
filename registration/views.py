from django.shortcuts import render
from registration.models import Manager, Canoe
from django.views.decorators.csrf import csrf_exempt
import random
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
    print 4
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
            print "Request: ", request
            for i in range (10,37):
                print "i:",i
                print request.POST["choice" + str(i)]
                responses[sessionID].append(request.POST["choice"+str(i)])
            print 'Responses', responses
    except(KeyError):
        print("Check try statement")
        return render(request, 'registration/register.html'), {'error_message': "You forgot to answer one or more questions"}
    
        
    if(section=="A"):
        
        following_section = "B"
        return render(request, "registration/register.html", {'section': following_section}) 
    elif (section=="B"):
        print"LOL"
        for x in range(len(responses[sessionID])):
            responses[sessionID][x] = str(responses[sessionID][x])
             
        hashe = random.getrandbits(6)
        
             
        print "Responses: ", responses
        m = Manager(name_of_fisher=responses[sessionID][0], date_of_birth=responses[sessionID][1], gender=responses[sessionID][2], occupation=responses[sessionID][3],
                    phone_number=responses[sessionID][4], email_address=responses[sessionID][5], manager_address=responses[sessionID][6], number_of_canoes=responses[sessionID][7])
        c = Canoe(canoe_id = hashe, isApproved=False, current_canoe_number=responses[sessionID][10], coastal_region=responses[sessionID][11],
                  coastal_district=responses[sessionID][12], fishing_village=responses[sessionID][13], landing_beach=responses[sessionID][14], current_canoe_name=responses[sessionID][15],
                  type_of_ownership=responses[sessionID][16], name_canoe_owner=responses[sessionID][17], name_captain=responses[sessionID][18], year_purchased=responses[sessionID][19],
                  year_built=responses[sessionID][20], place_built=responses[sessionID][21],first_year_fishing=responses[sessionID][22], construction_material=responses[sessionID][23],
                  length_overall=responses[sessionID][24],type_storage=responses[sessionID][25], crew_number=responses[sessionID][26], is_motorized=responses[sessionID][27], model_of_engine=responses[sessionID][28],
                  horsepower=responses[sessionID][29], first_gear_type=responses[sessionID][30], second_gear_type=responses[sessionID][31],third_gear_type=responses[sessionID][32],equipment_on_board=responses[sessionID][33],
                  date_of_registration=responses[sessionID][34], photo_one=responses[sessionID][35])
        m.save()
        c.save()
    return render(request, "registration/confirmation.html")
         
    
#===============================================================================
# def confirmation(request):
#     print"LOL"
#     for x in range(len(responses[sessionID])):
#         responses[sessionID][x] = str(responses[sessionID][x])
#          
#     hash = random.getrandbits(128)
#     six_char = "%006" % hash
#          
#     print "Responses: ", responses
#     m = Manager(name_of_fisher=responses[sessionID][0], date_of_birth=responses[sessionID][1], gender=responses[sessionID][2], occupation=responses[sessionID][3],
#                 phone_number=responses[sessionID][4], email_address=responses[sessionID][5], manager_address=responses[sessionID][6], number_of_canoes=responses[sessionID][7])
#     c = Canoe(Manager = m, manager_id = id, canoe_id = six_char,)
#      
#     return render(request, "registration/confirmation.html")
#===============================================================================

