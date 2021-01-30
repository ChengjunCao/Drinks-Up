from django.shortcuts import render
from django.http import HttpResponse
from .models import Drink


def home(request):
  return HttpResponse('<h1>Welcome to Drink It</h1>')

def drinks_index(request):
  drinks = Drink.objects.all()
  return render(request, 'drinks/index.html', { 'drinks': drinks})

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  return render(request, 'drinks/detail.html', { 'drink': drink})








