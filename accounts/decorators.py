from django.http import HttpResponse
from django.shortcuts import redirect

def admin_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.user_type == 'ادمین':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('شما اجازه دسترسی به این صفحه را ندارید')
    return wrapper_func