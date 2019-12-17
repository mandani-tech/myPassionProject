from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_user/', views.new_user, name='new_user'),
    path('login_my_user/', views.login_my_user, name='login_my_user'),
    path('log_me_out/', views.log_me_out, name='log_me_out'),
]
