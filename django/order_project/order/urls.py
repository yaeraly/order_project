from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('report/', views.ReportListView.as_view(), name='report'),
    path('menu/<int:pk>/', views.menu, name='menu'),
    path('del_b/<int:pk>/', views.BreakfastOrderDeleteView.as_view(), name='delete_b'),
    path('del_l/<int:pk>/', views.LunchOrderDeleteView.as_view(), name='delete_l'),
    path('del_d/<int:pk>/', views.DinnerOrderDeleteView.as_view(), name='delete_d'),


    # path('create/', views.RoomCreate.as_view(), name='create'),
    # path('delete/<int:pk>/', views.RoomDeleteView.as_view(), name='delete'),
    # path('create_db/', views.create_db, name='create_db'),
]
