from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):

    allowed_host=['127.0.0.1:8000']
    print("--->>>",type(request.get_host()))
    if(request.get_host() in allowed_host):
        return HttpResponse("Accessed by  Localhost :-> "+ str(request.get_host()))
    else:
        return HttpResponse("General host :-> "+request.get_host())