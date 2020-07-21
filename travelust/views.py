from django.shortcuts import render
from django.http import HttpResponse

from travelust.models import Destination


def home(request):
    dest1= Destination()
    dest2 = Destination()
    dest1.name = 'Bali'
    dest1.desc = 'nice place'
    dest1.price = 1000
    dest2.name = 'indonesia'
    dest2.desc = 'nicest place'
    dest2.price = 500

    return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2})
