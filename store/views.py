from django.shortcuts import render
from .models import Products, Category
from django.core.paginator import Paginator
# Create your views here.
 
def index(request):
    product_objects = Products.objects.all()
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Products.objects.filter(category=category_id) #sortuje produkty wedlug kategorii
    else:
        products = Products.objects.filter(category=1) #sortuje domyslnie

    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
         product_objects = product_objects.filter(title__icontains=item_name)
 
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request,'store/index.html',{'product_objects':product_objects, 'categories':categories})

# def search(request):
#     item_name = request.GET.get('item_name')
#     if item_name != '' and item_name is not None:
#          product_objects = product_objects.filter(title__icontains=item_name)
#     return render(request,'store/index.html',{'product_objects':product_objects,})    

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'store/detail.html', {'product_object':product_object})

def home(request):
    products_objects = Products.objects.all()
    categories = Category.objects.all()
    context = {'products_objects': products_objects, 'categories': categories}
    return render(request, 'store/home.html', context)


