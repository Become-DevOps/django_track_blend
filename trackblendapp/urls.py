from django.urls import path 
from trackblendapp import views 

app_name = "trackblendapp"

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('home',views.home,name='home'),
]
