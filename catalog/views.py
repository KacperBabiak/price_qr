from django.shortcuts import render
from django.template import RequestContext
from .models import Product

def index(request):
    """View function for home page of site."""
    idx=0

    num_products = Product.objects.all().count()
    products = Product.objects.all()
    
    price = products[idx].price 

        
    try:
        data = request.POST
        name = data.get("product_select")


    except:
        name = products[idx].name 
        

    finally:
        context = {
            'num_products' : num_products,
            'products' : products,
            'name' : name,
            'price' : price,
        }
        return render(request,'index.html', context = context)



   