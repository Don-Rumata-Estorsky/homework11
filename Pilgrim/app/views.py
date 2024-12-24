from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *


from django.http import JsonResponse
import random


def viewer(request):
    
    num = random.sample(range(1, 11), 10)

    return JsonResponse(num, safe=False)


def viewhtml(request):
    return render(request, 'a1.html')

