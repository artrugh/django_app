from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey there")


def post(request):
    return HttpResponse("I am a single post page.")
