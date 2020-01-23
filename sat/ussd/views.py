from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#import africastalking
from ussd.models import User
#from mob_checkout import *


@csrf_exempt
def index(request):
    print("Received request!")
    session_id = request.POST.get("sessionId", None)
    service_code = request.POST.get("serviceCode", None)
    phone_number = request.POST.get("phoneNumber", None)
    text = request.POST.get("text", "default")
    print("text:", text)

    if phone_number is None:
        return HttpResponse("invalid request, no phone number provided")
    try:
        response = ""
        user = User.objects.get(pk=phone_number)
        print("user with phone number {} does exist".format(phone_number))
        if not text:
            print("test in")
            response = "CON Welcome to Growsearch \n"
            response += "1. My Account \n"
            response += "2. My phone number"
        elif text == '1':
            response = "CON Choose account information you want to view \n"
            response += "1. Account number \n"
            response += "2. Account balance"
        elif text == '1*1':
            accountNumber = "ACC1001"
            response = "END Your account number is " + accountNumber
        elif text == '1*2':
            balance = "KES 10,000"
            response = "END Your balance is " + balance
        elif text == '2':
            response = "END This is your phone number " + phone_number
        return HttpResponse(response)

    except User.DoesNotExist:
        print("User doesnot exist")
        if not text:
            print("test in")
            response  = "CON Welcome to Growsearch \n"
            response += "1. Register \n"
            response += "2. Sign in"
        elif text[0] == "1":
            if text.count('*') == 0:
                print("Entered 1")
                response = "CON Welcome to the registration portal,\n enter your fullname"
            elif text.count('*') == 1:
                print("Entered != ''")
                response = "CON enter the Tel_No \n"
            #elif text.count('*') == 2:
                #print("Entered 1*1")
                #store the tel no in database
                #response = "CON enter your status \n"
                #response += "1.buyer \n"
                #response += "2.farmer"
            elif text.count("*") == 2:
                print("Entered 1*1*1")
                #store the status
                response = "CON enter the location \n"
            #elif text.count('*') == 4:
                #print("Entered 1*1*1*1")
                #store the location
                #response = "CON generate a password \n"
            elif text.count('*') == 3:
                print("Entered 1*1*1*1*1")
                #store the password
                response = "CON the subscription fee is 20,000UGX per year \n"
                response += "1.enter subscription fee \n"
                response += "2.exit"

            elif text.count('*') == 4:
                print("Entered 1*1*1*1*1*1")
                if text[-1] == "1":
                #try:
                    #res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
                    #print(res)
                #except Exception as e:
                    #print(f"Houston we have a problem {e}")
                #save data to database
                    response = "END thank you for registering\n we will keep you updated "
                elif text[-1] == "2":
                    response = "END waiting to hear from you soon"
        elif text[0] == "2":
            if text.count('*') == 0:
                print("Entered 2")
                response = "CON enter your password \n"
            elif text.count('*') == 1:
                print("Entered != ''")
                response = "CON buying or selling \n"
                response += "1. selling \n"
                response += "2. buying"
            elif text.count('*') == 2:
                print("Entered 2*1")
                response = "CON enter details of Produce \n"
            elif text.count('*') == 3:
                print("Entered 2*2")
                response = "END thank you!! we will get back to you soon"

    return HttpResponse(response)




    """response = ""
    if not text:
        print("test in")
        response  = "CON Welcome to Growsearch \n"
        response += "1. My Account \n"
        response += "2. My phone number"
    elif text == '1':
        response = "CON Choose account information you want to view \n"
        response += "1. Account number \n"
        response += "2. Account balance"
    elif text == '1*1':
        accountNumber  = "ACC1001"
        response = "END Your account number is " + accountNumber
    elif text == '1*2':
        balance  = "KES 10,000"
        response = "END Your balance is " + balance
    elif text == '2':
        response = "END This is your phone number " + phone_number
    return HttpResponse(response)"""


#def request_handler(request)
#am i supposed to declare new variables or i use the previous variables
#how do i store the data in database(learn arrays)
#how to collect input from the user(text input)
#meaning of request.POST.get in django input or output
#what is the meaning of explode
#text = request.get("text", "default")
#if not text:
#print ("test in")
#response  = "CON Welcome to Growsearch \n"
    	#response += "1. Register \n"(fullname,Tel_No,status,location,password,$subscription)
    	#response += "2. Sign in"
   # elif text == '1':
   #response = "CON Welcome to the registration portal,\n enter your fullname"
   #elif text != ""
   #response = "CON enter the Tel_No \n"
   #elif text != ""
   #response = "CON enter your status \n"
   #response += "1.buyer
   #response += "2.seller
   #elif text != ""
   #response = "CON enter the location \n"
   #elif text != ""
   #response = "CON generate a password \n"
   #elif text != ""
   #response = "algorithm for subscription"
   #elif text != ""
   #save data to the database using an array or lists
   #response = "END thank you for registering\n we will keep you updated "
   #return HttpResponse(response)

   #elif text =="2"
   #response = "CON enter your password \n"
   #elif text != ""
   #response += "1. selling
   #response += "2. buying
   #elif text == "2*1" or !=""
   #response = "CON enter details of Produce \n"
   #elif text !=""
   #response == "END thank you!! we will get back to you soon"
   #elif
    #return HttpResponse(response)

#from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt

#response = ""

#@csrf_exempt
#def ussd_callback(request):
    #global response
    #if(request.method == 'GET' or request.method == 'POST'): 
        #test = request.POST.dict()
        #session_id = test.get("sessionId", None)
        #service_code = test.get("serviceCode", None)
        #phone_number = test.get("phoneNumber", None)
        #text = test.get("text", "default")
        #    return HttpResponse("This is a post request")   

        #if text == ' ':
            #response = "CON What would you want to check \n"
            #response += "1. My Account \n"
            #response += "2. My phone number"
        #elif text == '1':
            #response = "CON Choose account information you want to view \n"
            #response += "1. Account number \n"
            #response += "2. Account balance"
        #elif text == '1*1':
            #accountNumber = "ACC1001"
            #response = "END Your account number is " + accountNumber
        #elif text == '1*2':
            #balance = "KES 10,000"
            #response = "END Your balance is " + balance
        #elif text == '2':
            #response = "This is your phone number " + phone_number
        #return HttpResponse(response)
    #else:
        #print("this is not a post request", request)"""
    # Create your views here.
