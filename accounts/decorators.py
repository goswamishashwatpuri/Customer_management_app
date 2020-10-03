from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func    

def allowed_users(allowed_roles = []):

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
                #type of group is <class 'django.contrib.auth.models.Group'>, hence first convert to string !!!!
                if str(group) in allowed_roles:
                    return view_func(request, *args, **kwargs)
                elif str(group) == 'user':
                    return redirect('user_page')
                else:
                    return HttpResponse("sorry not sorry")
            

        return wrapper_func
    return decorator





#just a quick fix for if : USER clicks on dashboard, he'll see the "NOT AUTHORISED" message and will have nowhere to navigate to

# def admin_only(view_func):

#     def wrapper_func(request, *args, **kwargs):
#         group = None

#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name

#         print('-----------',group)
#         if str(group) == 'user':
#             return redirect('user_page')
#         if str(group) == 'admin':
#             return view_func(request, *args, **kwargs)
        
#     return wrapper_func




