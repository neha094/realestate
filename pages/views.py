from django.shortcuts import render
from django.http import HttpResponse
from listings.models import listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    dests = listing.objects.order_by('-list_date').filter( is_published = True)[:3]
    context = {
        'dests': dests
    }
    return render(request,'index.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # Get MVP
    dests = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'dests': dests
    }
    return render(request,'about.html',context)

