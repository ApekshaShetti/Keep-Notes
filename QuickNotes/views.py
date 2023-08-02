from django.shortcuts import render,redirect
from django.http import JsonResponse

# Create your views here.

def getRoutes(request):
    return JsonResponse('Our App',safe=False)
