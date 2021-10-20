from django.urls import path
from . import views

urlpatterns = [
            path('registration', views.registration, name='registration'),
            path('login', views.loginauth, name='login'),
            path('logout', views.logoutPage, name='logout'),

            path('', views.homepage, name = 'homepage'),
            path('account/', views.accountSetting, name = 'account'),
            path('product/', views.product, name='product'),
            path('customer/<str:pk>/', views.customer, name='customer'),
            path('user', views.userinterface, name='user-page'),
            
            path('create_order/<str:pk>/', views.createOrder, name= 'create_order'),
            path('update_order/<str:pk>/', views.UpdateOrder, name= 'update_order'),
            path('delete_order/<str:pk>/', views.DeleteOrder,name='delete_order'),
            
            
]
