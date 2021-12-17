from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users , admin_only
from django.contrib.auth.models import Group

# Create your views here.
@unauthenticated_user
def registration(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Customer.objects.create(
                user=user,
                )

            messages.success(request, 'Account was created for ' + username )
            return render(request,'welcome.html')

    context = {'form':form}
    return render(request,'registration.html',context)

def loginauth(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            paasword = request.POST.get('password')

            user = authenticate(request, username=username, password=paasword)
            
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request,'Username or Password is incorrect')
                
        # return render(request, 'login.html')
        return render(request,'welcome.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def homepage(request):
    customers = Customer.objects.all()

    orders = Order.objects.all()
    total_order = orders.count()

    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'customers': customers,'total_order':total_order,'orders':orders, 
    'delivered':delivered,'pending':pending}

    return render(request,'homepage.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def product(request):
    products = Product.objects.all()
    return render(request,'product.html',{'products': products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    current_customer = Customer.objects.get(id=pk)
    current_user_order = current_customer.order_set.all()
    total_order_by_user= current_user_order.count()
    context = {'customer':current_customer, 'order':current_user_order, 'total_order':total_order_by_user}
    return render(request,'customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    
    return render(request,'create_order.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateOrder(request,pk): 
    order =Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request,'create_order.html', context )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def DeleteOrder(request,pk):
    order =Order.objects.get(id=pk)
    if request.method =='POST':
        order.delete()
        return redirect ('homepage')
    context={'item':order}
    return render(request, 'deleteorder.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userinterface(request):
    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context= {'order': orders ,'total_order':total_order,'orders':orders,'delivered':delivered,'pending':pending}
    return render(request, 'user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSetting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form =CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'accountsettings.html', context)