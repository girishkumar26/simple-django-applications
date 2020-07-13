from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'basics without css'})


def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = 0

    try:
        if 'on' in request.GET['sum']:
            res = val1 + val2
    except Exception as e:
        pass

    try:
        if 'on' in request.GET['sub']:
            res = val1 - val2
    except Exception as e:
        pass

    try:
        if 'on' in request.GET['mul']:
            res = val1 * val2
    except Exception as e:
        pass

    try:
        if 'on' in request.GET['div']:
            res = val1 / val2
    except Exception as e:
        pass

    return render(request, 'home.html', {'result': res})
