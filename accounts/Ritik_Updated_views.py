# Ritik Kochar
# github link : https://github.com/RitikKochar0509
# Btech : 3rd year IT

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .decorators import unauthenticated_user, allowed_users #admin_only
from .models import *
from .forms import order_form, user_registeration_form, user_settings
from .filters import order_filter


# Create your views here.

@unauthenticated_user
def login_page(request):

    if request.method == 'POST':

       # the username and passowrd used insode get() method are with the help of 
       # request, which is sent  by the template, name='' property stores the username & password (basically the value through form)
       # check name='' value in login.html for more info

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            #throw the request and user object to login()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect') 
    
    context = {}
    return render(request, 'login.html', context)        


def logout_page(request):

    logout(request) 
    return redirect('login')    


@unauthenticated_user
def register(request):

    form = user_registeration_form()

    if request.method == 'POST' :

        form = user_registeration_form(request.POST)
        
        if form.is_valid():
            user = form.save()
 
            #username = form.cleaned_data.get('username')
            messages.success(request, 'User has been created.')
            return redirect('/login')

    context = {
        'form' : form,
    }

    return render(request, 'register.html', context)    



@login_required(login_url='/login/')
@allowed_users(allowed_roles = ['user'])
def user_page(request):

    orders = request.user.customer.order_set.all()

    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for Delivery').count()

    context = {

        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'Out for Delivery': out_for_delivery,
    }
    return render(request, 'user_page.html', context)

    
@login_required(login_url='login')
@allowed_users(allowed_roles = ['user'])
def user_settings_page(request):
    
    user = request.user.customer
    form = user_settings(instance=user)

    if request.method == 'POST':
        form = user_settings(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {
        'form' : form
    }
    return render(request, 'user_settings.html', context)
     




@login_required(login_url='/login/')
@allowed_users(allowed_roles = ['admin'])
def home(request):
      
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    out_for_delivery = orders.filter(status='Out for Delivery').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'Out for Delivery': out_for_delivery,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login/')
def products(request):

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# customer page view
@login_required(login_url='/login/')
def customers(request, customer_id):

    individual_customer = Customer.objects.get(id=customer_id)
    orders = individual_customer.order_set.all()
    order_count = orders.count()

    search_filter = order_filter(request.GET, queryset=orders )
    orders = search_filter.qs

    context = {
        'customer': individual_customer,
        'orders': orders,
        'order_count': order_count,
        'search_filter' : search_filter,
    }

    return render(request, 'customers.html', context)


# put create_order snippet below this comment
## Added Code
@login_required(login_url='/login/')
def create_order(request, customer_id):

    order_form_set = inlineformset_factory(Customer, Order, fields=('Product','status'), extra=10)
    customer = Customer.objects.get(id=customer_id)
    
    # formset is instance of order_form_set
    formset = order_form_set(queryset= Order.objects.none(), instance=customer)
    # form = order_form(initial={'Customer' : customer})
    context = {
        'formset' : formset,
        'customer_id' : customer_id,
    }

    if request.method == 'POST':

        #form = order_form(request.POST)
        formset = order_form_set(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect(f'/customers/{customer.id}')

    return render(request, 'order_form.html', context)




# put update and delete order snippets below this comment 
