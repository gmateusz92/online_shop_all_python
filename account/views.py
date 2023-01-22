from django.shortcuts import render, redirect
# from .models import Cart, Products, CartItem

# def login(request):
#     if request.method == "GET":
#         return render(request, 'store/login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_msg = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 request.session['customer_id'] = customer.id
#                 request.session['email'] = customer.email
#                 return redirect("home")
#             else:
#                 error_msg = "Email or Password is incorrect."
#         else:
#             error_msg = "Email or Password is incorrect."
#         return render(request, 'store/login.html', {'error_msg': error_msg})

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')