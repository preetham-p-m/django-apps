from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def homepage(request):
    return HttpResponse('Home Page')
