from django.shortcuts import render,get_object_or_404
from .models import listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def index(request):
    dests = listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(dests, 6)
    page = request.GET.get('page')
    paged_dests = paginator.get_page(page)

    context = {
        'dests': paged_dests
    }
    return render(request,'listings.html', context)

def listin(request, listin_id):
    dests = get_object_or_404(listing, pk=listin_id)
    context={
        'dests': dests
    }
    return render(request,'listing.html',context)

def search(request):
    return render(request,'search.html')
