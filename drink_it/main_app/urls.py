from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('drinks/', views.drinks_index, name='index'),
      path('drinks/<int:drink_id>/', views.drinks_detail, name='detail')

]