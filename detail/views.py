import dress as dress
from django.shortcuts import render
from shop.models import bottom, dress, top, outer
# Create your views here.

def bott(request):
    bottoms = bottom.objects.all().order_by('pk')
    return render(request, 'bottom.html', {'bottoms':bottoms})

def dre(request):
    dresss = dress.objects.all().order_by('pk')
    return render(request, 'dress.html', {'dresss':dresss})

def out(request):
    outers = outer.objects.all().order_by('pk')
    return render(request, 'outer.html', {'outers':outers})

def to(request):
    tops = top.objects.all().order_by('pk')
    return render(request, 'top.html', {'tops':tops})