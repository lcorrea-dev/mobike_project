from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    bicycles = []
    return JsonResponse(bicycles, safe=False)
