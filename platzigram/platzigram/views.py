"""platzigram views"""
from django import http
from django.http import HttpResponse, response
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%dth %b, %Y - %H:%M hrs')
    return HttpResponse('OLAAA TU FECHA es {now}'.format(now=str(now)))

def hi(request):
    #esto es un debugger import pdb; pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'numbers cool',
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
        )

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {} no eres mayor de edad:c'.format(name)
    else: message = 'HOLAAA {} bienvenido'.format(name)
    return HttpResponse(message)