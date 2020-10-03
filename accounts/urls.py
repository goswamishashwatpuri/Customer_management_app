from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home' ),
    
    path('user_page/', views.user_page, name='user_page'),
    path('user_settings/', views.user_settings_page, name='user_settings'),

    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('customers/<str:customer_id>/', views.customers, name='customer'),
    path('products/', views.products, name='products'),

    path('update_order/<str:order_id>/', views.update_order, name='update_order' ),
    path('delete_order/<str:order_id>/', views.delete_order, name='delete_order' ),
    path('create_order/<str:customer_id>/', views.create_order, name='create_order'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

]