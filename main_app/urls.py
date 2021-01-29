from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    path('accounts/signup/', views.signup, name='signup'),

]
