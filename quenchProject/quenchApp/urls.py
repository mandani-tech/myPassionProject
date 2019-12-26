from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('new_user/', views.new_user, name='new_user'),
    path('login_my_user/', views.login_my_user, name='login_my_user'),
    path('log_me_out/', views.log_me_out, name='log_me_out'),
    path('product_list_view/', views.product_list_view, name='list'),
    path('product_detail_view/<int:pk>/', views.product_detail_view, name='detail'),


    path('my_cart/', views.my_cart, name='my_cart'),
    path('cart_update/', views.cart_update, name='cart_update'),



]

