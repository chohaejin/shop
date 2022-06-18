from django.shortcuts import render
from shop.models import Good

# Create your views here.

def shop(request):
    goods = Good.objects.all().order_by('pk')
    return render(request, 'base.html', {'goods':goods})
