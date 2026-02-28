from django.http import HttpResponse

def homePage(request):
    print("THis is checking for views.py ")
    return HttpResponse("My name is satyam")