from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, reverse
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


#
# class ProductDetailView():
# #     queryset = Product.objects.all()
#     template_name = "quenchApp/detail.html"

#     def get_context_data(self,*args,**kwargs):
#         context =super(ProductDetailView, self).get_context_data(*args,**kwargs)
#         print(context)
#         return (context)
#
#     def get_object(self,*args,**kwargs):
#         request = self.request
#         pk= self.kwargs.get(pk)
#         instance = Product.objects.get(pk)
#         if instance is None:
#             raise Http404("Product doesn't Exits")
#         return instance

def product_detail_view(request, pk):
#
    instance = get_object_or_404(Product, pk=pk)
#     instance = Product.objects.get(pk)
#     if instance is None:
#                 raise Http404("Product doesn't Exits")
    context={
    'object': instance,
    'pk': pk

    }
    return render (request,"quenchApp/detail.html", context)










def search_results(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        print(query)
    context = {
        'list': Product.objects.filter(Q(itemName__contains= query ) | Q(dept__contains = query)),

    }

    return render(request,'quenchApp/search_results.html',context)




#___________________________________________Shopping cart_____________________________

#
#
# def cart_create(user=None):
#     cart_obj=Cart.objects.create(user=None)
#     print('New Cart ID created')
#     return cart_obj



def my_cart(request):
#
#     del request.session['cart_id']
    cart_id = request.session.get("cart_id", None) #_______________________ get the current cart_id  or set it to None .
    qs = Cart.objects.filter(id=cart_id) #__________________________________query set or instantiate  Cart Model  using the filter for this session
    if qs.count() == 1: #___________________________________________________ when the cart_obj is created this is the first row in the table and its count will be equal to 1
        print (request.user)
        print('Cart ID Exits') #____________________________________________ if user clicks the my cart again the cart id already is existing for this session
        print(cart_id) # _____________________________________________________console will print this cart id for this session
        cart_obj = qs.first() # ______________________________________________cart_obj will be equal to the first row in the table and we will ignore any other rows i Cart table
        if request.user.is_authenticated and cart_obj.user is None:
            print (request.user)
            cart_obj.user = request.user # ____________________________________associate the cart with the logged in user
            cart_obj.save() # _________________________________________________save new cart object
            print(cart_id, cart_obj)
    else:
            cart_obj = Cart.objects.new(request,user=request.user) # __________________creating new cart object for the current user
            request.session['cart_id'] = cart_obj.id #_________________________Associate current session with the users cart for logged in user
            print(cart_id)

    products = cart_obj.products.all()
    total = 0
    for x in products:
        total+=x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'quenchApp/my_cart.html',{"cart":cart_obj})




def cart_update(request):

    product_id = request.POST.get('product_id')  # from the form product.id is requested
    print(product_id)
    if product_id is not None: # if this product is in inventory
        try:
            product_obj = Product.objects.get(id=product_id) # grab the product_obj for product_id
        except Product.DoesNotExist:
            print("Show message to user, product is gone")
            return redirect ("my_cart")
#         cart_obj  = Cart.objects.new(request,user = request.user)  # create new cart_obj
        cart_obj  = Cart.objects.get(user = request.user)
        if product_obj in cart_obj.products.all(): # if this product is in cart
            cart_obj.products.remove(product_obj) # remove the product from cart

        else:
            cart_obj.products.add(product_obj) # add the product to the cart
#               cart_obj.products.add(obj)#cart_obj.products.add(product_id)
    return redirect ("my_cart") # redirects to cart

#
# def cart_update(request, pk):
#     cart = Cart.objects.all()[0]
#     try:
#         product_obj = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         pass
#     except:
#         pass
#     if not product in cart.products.all():
#         cart.products.add(product)
#     else:
#         cart.products.remove(product)
#     return HttpResponseRedirect(reverse("/my_cart/"))







#________________________________________________ Creating a sign up user
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
