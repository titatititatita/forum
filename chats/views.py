from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi! Welcome to our small project. Don't be shy, let's chat!")
