from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Drink
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def main(request):
  return render(request, 'main.html')

def home(request):
  drinks = Drink.objects.filter(user=request.user)
  return render(request, 'home.html', {'drinks': drinks})

def drinks_index(request):
  drinks = Drink.objects.filter(user=request.user)
  return render(request, 'drinks/index.html', {'drinks': drinks})

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  return render(request, 'drinks/detail.html', {'drink': drink})

class DrinkCreate(CreateView):
  model = Drink
  fields = ['name', 'type', 'description', 'rating', 'price']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DrinkUpdate(UpdateView):
  model = Drink
  fields = ['type', 'price', 'description']


class DrinkDelete(DeleteView):
  model = Drink
  success_url = '/drinks/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
