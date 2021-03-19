from django.urls import path
from . import views

app_name = 'user_login'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    

]