
from django.http import HttpResponse
from django.shortcuts import redirect


def admin_permission_decorator(func,request):
    if request.user.is_staff:
        func()
    else:
        return redirect('login_view')



