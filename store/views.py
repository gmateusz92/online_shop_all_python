from django.shortcuts import render, redirect
from .models import Products, Category
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
 
def index(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart: #jesli koszyk zostal utworzony
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else: #jesli koszyk nie zostal utowrzony tworzy nowy koszyk
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('home')

    else:
        product_objects = None
        #product_objects = Products.objects.all()
        categories = Category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
            products_objects = Products.objects.filter(category=category_id) #sortuje produkty wedlug kategorii
        else:
            products_objects = Products.objects.filter(category=1) #sortuje domyslnie

        # if request.method == 'POST':
        #     product = request.POST.get('product')
        #     cart = request.session.get('cart')
        #     if cart:
        #         quantity = cart.get(product)
        #         if quantity:
        #             cart[product] = quantity + 1
        #         else:
        #             cart[product] = 1
        #     else:
        #         cart = {}
        #         cart[product] = 1

        #     request.session['cart'] = cart
        #     print(request.session['cart'])
        #     return redirect('home')

        # else:
        #     products = None
        #     categories = Category.objects.all()
        #     category_id = request.GET.get('category')
        #     if category_id:
        #         products = Products.objects.filter(category=category_id)
        #     else:
        #         products = Products.objects.filter(category=1)
        #     context = {'products': products, 'categories': categories}
        #     print("Your Email Address is: ", request.session.get('email'))
        #     return render(request, 'store/index.html', context)

        #search code
        # item_name = request.GET.get('item_name')
        # if item_name != '' and item_name is not None:
        #     product_objects = product_objects.filter(title__icontains=item_name)
    
        #paginator code
        # paginator = Paginator(product_objects,4)
        # page = request.GET.get('page')
        # product_objects = paginator.get_page(page)
        
        return render(request,'store/index.html',{'product_objects':product_objects, 'categories':categories})
        #return HttpResponse("Hello")

def search(request):
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
         product_objects = product_objects.filter(title__icontains=item_name)
    return render(request,'store/index.html',{'product_objects':product_objects,})    

def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render(request, 'store/detail.html', {'product_object':product_object})

def home(request):
    products = None
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Products.objects.filter(category=category_id)
    else:
        products = Products.objects.filter(category=1)
    context = {'products': products, 'categories': categories}
    return render(request, 'store/home.html', context)


