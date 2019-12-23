from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Sign_Up_UserForm, Sign_In_UserForm
from django.contrib.auth.models import User
from .models import Cart, Product

from django.contrib.auth import login, authenticate, logout

def index(request):
    return render(request, 'quenchApp/index.html')


def home(request):
#         print(request.session.get("first_name","unknown"))
        return render(request, 'quenchApp/home.html')


#______________________________________Product Views_____________________

def product_list_view(request):
    queryset =Product.objects.all()
    context={
    'object_list': queryset,

    }
    return render (request,"quenchApp/list.html", context)


def product_detail_view(request, pk):
#     instance = Product.objects.filter( pk = pk )
    instance = get_object_or_404(Product, pk=pk)
    context={
    'object': instance,
    'pk': pk

    }
    return render (request,"quenchApp/detail.html", context)


# def product_detail_view(request,pk):
#     instanceOfProduct = Product.objects.get(pk=pk)
#
#     context = {
#         'object': instanceOfProduct,
#         'pk': request.user.pk
#     }
#     return render(request,'wikiApp/details.html',context)
#

















#___________________________________________Shopping cart_____________________________
def cart_create(user=None):
    cart_obj=Cart.objects.create(user=None)
    print('New Cart ID created')
    return cart_obj


def my_cart(request):
    request.session['cart_id'] ="12"
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        cart_obj=cart_create()
        request.session['cart_id'] = cart_obj.id

    else:
        qs=Cart.objects.filter(id=cart_id) #qs is the query set variable
        if qs.count() ==1:
            print('Cart ID exists')
            print(cart_id)
            cart_obj = qs.first()
        else:
            cart_obj = cart_create()
            request.session['cart_id'] =cart_obj.id
    return render(request, 'quenchApp/my_cart.html',{})




def cart_update(request):
    product_id =1
    product_obj = Product.objects.get(id=product_id)
    cart_obj ,new_obj = Cart.objects.new_or_get(request)
    cart_obj.products.add(obj)#cart_obj.products.add(product_id)
    return redirect ("my_cart")








# Creating a sign up user
def new_user(request):
    if request.method == "POST":
        newUser = Sign_Up_UserForm(request.POST)
        if newUser.is_valid():
            logInUser = User.objects.create_user(first_name=request.POST['first_name'],
                                                 last_name=request.POST['last_name'],
                                                 username=request.POST['username'],
                                                 password=request.POST['password'],)
            login(request, logInUser)
            return redirect("index")
        else:
            context = {
                "errors": newUser.errors,
                "form": Sign_Up_UserForm(),
            }
            return render(request, 'quenchApp/new_user.html', context)
    else:
        context = {
            "form": Sign_Up_UserForm
        }
        return render(request, 'quenchApp/new_user.html', context)





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
                    "loginform": Sign_In_UserForm,
                }
                return render(request, "quenchApp/login_my_user.html", context)


       context = {

            "loginform": Sign_In_UserForm,
       }
       return render(request, "quenchApp/login_my_user.html", context)




def log_me_out(request):
    logout(request)
    return redirect("index")
