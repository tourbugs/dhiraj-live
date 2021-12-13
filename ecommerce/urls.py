from django.urls import path

from django.contrib.auth import views as auth_views

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

            path('reset_password/', 
                auth_views.PasswordResetView.as_view(template_name="reset_password.html"), 
                name="reset_password"),

            path('reset_password_sent/', 
                auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
                name="password_reset_done"),

            path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),

            path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
            


            
            
            
]
