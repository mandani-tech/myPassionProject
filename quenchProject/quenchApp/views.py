from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
    return render(request, 'quenchApp/index.html')



# Creating a sign up user
def new_user(request):
    if request.method == "POST":
        newUser = NewUserForm(request.POST)
        if newUser.is_valid():
            logInUser = User.objects.create_user(username=request.POST['username'],
                                                 password=request.POST['password'])
            login(request, logInUser)
            return redirect("index")
        else:
            context = {
                "errors": newUser.errors,
                "form": NewUserForm(),
            }
            return render(request, 'quenchApp/new_user.html', context)
    else:
        context = {
            "form": NewUserForm()
        }
        return render(request, 'quenchApp/new_user.html', context)




# def login_my_user(request):
#
#     context={
#     "loginform": NewUserForm()
#     }
#     return render(request, 'quenchApp/login_my_user.html', context)




def login_my_user(request):
       if request.method == "POST":
            loggedInUser = authenticate(username = request.POST['username'], password = request.POST["password"])
            if loggedInUser is not None:
                login(request, loggedInUser)
                return redirect("index")
            else:
                messages.error(request, "Wrong username or password")
                return redirect("login_my_user")

                # *** This is a different way you can send an error message and rerender the login_user page ***
                context = {
                    "error": "Wrong username or password",
                    "loginform": NewUserForm,
                }
                return render(request, "quenchApp/login_my_user.html", context)


       context = {

            "loginform": NewUserForm,
       }
       return render(request, "quenchApp/login_my_user.html", context)




def log_me_out(request):
    logout(request)
    return redirect("index")
