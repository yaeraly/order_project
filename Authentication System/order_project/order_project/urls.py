"""order_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from order import views as order_views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.login_view, name='login'),


    path('home/', order_views.HomeListView.as_view(), name='home'),
    path('create/', order_views.RoomCreate.as_view(), name='create'),
    path('delete/<int:pk>/', order_views.RoomDelete.as_view(), name='delete'),


    path('register/', account_views.register_view, name='register'),

    path('logout/', account_views.LogoutView.as_view(), name='logout'),
    path('passwd_change/', account_views.PasswdChangeView.as_view(), name='password_change'),
    path('passwd_reset/', account_views.PasswordResetView.as_view(), name='password_reset'),
    path('passwd_reset/done/', account_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', account_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
