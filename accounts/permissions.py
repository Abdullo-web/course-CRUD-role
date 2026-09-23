from django.shortcuts import render,redirect
# from functools import wraps
def permission_required(*role):
    def dec(func):
        def inner(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return render(request, 'not_permissions.html',)
            if request.user.role in role:
                return func(request,*args, **kwargs)
            return render(request,'not_permissions.html',)  
        return inner
    return dec


# from django.shortcuts import render,redirect
# from functools import wraps
# def permission_required(*role):
#     def dec(func):
#         @wraps(func)
#         def inner(request, *args, **kwargs):
#             if not request.user.is_authenticated:
#                 return render(request, 'not_permissions.html', status=403)
#             if request.user.role in role:
#                 return func(request,*args, **kwargs)
#             return render(request,'not_permissions.html',status=403)  
#         return inner
#     return dec
