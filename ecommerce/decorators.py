from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_funtion(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_funtion

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_funtion(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request,*args,**kwargs)
            else:
                return HttpResponse(' You are not authorized to view this page.')
        return wrapper_funtion
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('user-page')
        if group == 'admin':
            return view_func(request,*args,**kwargs)
    return wrapper_func