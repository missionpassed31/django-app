from django.shortcuts import render
from django.http import HttpResponse
import pyotp
import time

def sayhello(request):
    totp = pyotp.TOTP("UnwantedSoul273")
    return HttpResponse(totp.now())
   

    # return HttpResponse("Hello world")
# Create your views here.
