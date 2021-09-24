from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home/',views.home,name='main'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('registration/',views.userCreate,name='register'),
]