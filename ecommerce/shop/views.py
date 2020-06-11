from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    # products=Product.objects.all()
    # n=len(products)
    # print(products)
    # nSlides=n//4+ceil((n/4)-(n//4))
    # params={'slides':nSlides, range:(1,nSlides), 'product':products}
    # allProds=[[product.object.va,range(1,len(nSlides),nSlides)],
    #           [product.object.value(category='electronics'), range(1,len(nSlides),nSlides)]]
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("At contact")

def tracker(request):
    return HttpResponse("At tracker")

def search(request):
    return HttpResponse("At search")

def productView(request):
    return HttpResponse("At Product view")

def checkout(request):
    return HttpResponse("At checkout")