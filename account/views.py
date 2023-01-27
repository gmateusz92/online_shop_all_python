from django.shortcuts import render, redirect
from .models import Customer
from django.http import HttpResponse

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
    if request.method == 'GET':
        return render(request, 'store/signup.html')
    else:
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

        values = { #wyswietla wartosci zapisane w formularzu po wypelnieniu i odswiezeniu nie znikaja
            'firstname': first_name,# cos nie dziala
            'lastname': last_name,
            'phone': phone,
            'email': email,
        }

        err_msg = None

        if not first_name:
            err_msg = "First Name Required."
        elif len(first_name) < 3:
            err_msg = "First Name must be 3 characters long."
        elif not last_name:
            err_msg = "Last Name Required."
        elif len(last_name) < 3:
            err_msg = "Last Name must be 3 characters long."
        elif not phone:
            err_msg = "Phone is Required."
        elif len(phone) < 10:
            err_msg = "Phone Number must be 10 characters long."
        elif not email:
            err_msg = "Email is Required."
            return HttpResponse("<h3>succcccck</h3>")
        elif customer.does_exits():
            err_msg = "User with this email address already registered."    
        if not err_msg:
            customer.save()
            #return redirect('index')
            return HttpResponse("<h3>success</h3>")
        else:
            return render(request, 'store/signup.html', {'error_msg': err_msg, 'values': values})
            #return HttpResponse("<h3>xxxx</h3>")