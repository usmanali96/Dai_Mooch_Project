#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from products.models import Products
from carousel.models import Carousel

def  home(request):

    productsData = Products.objects.all()
    carousel = Carousel.objects.all()

    print(productsData)

    data = {
        "products": productsData,
        "carousel": carousel
        }
             
    return render(request, 'home.html', data)


def  about(request):
    return render(request, 'aboutus.html',)
