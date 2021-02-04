from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.home, name='home'),
    path('drinks/', views.drinks_index, name='index'),
    path('drinks/<int:drink_id>/', views.drinks_detail, name='detail'),
    path('drinks/create_page/', views.create_page, name='create_page'),
    path('drinks/create_drink/', views.create_drink, name='drink_form'),
    path('drinks/<int:drink_id>/update/', views.update_page, name='update_page'),
    path('drinks/<int:drink_id>/update_drink/', views.update_drink, name='update_drink'),
    # path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete'),

    path('search', views.search_page, name='search'),
    path('search/result', views.search_result, name='result'),

    path('accounts/signup/', views.signup, name='signup'),
]
