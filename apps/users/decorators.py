from django.urls import reverse_lazy
from django.shortcuts import redirect

def login_excluded(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy("users:profile"))
        
        return function(request, *args, **kwargs)

    return wrap