from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('passwd_change/', views.PasswdChangeView.as_view(), name='password_change'),
    path('passwd_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('passwd_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
