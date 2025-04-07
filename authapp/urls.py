from django.urls import path
from .views import login_view, register_view, dashboard_view, error_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('error/', error_view, name='error'),
    path('logout/', logout_view, name='logout'),
]