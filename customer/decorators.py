from django.shortcuts import redirect
from django.contrib.auth.models import User

def sign_in_required(fun):
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fun(req,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper

def owner_permission_required(fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return fun(request,*args,**kwargs)
        else:
            return redirect("signin")
    return wrapper