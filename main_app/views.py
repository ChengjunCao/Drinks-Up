from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Drink
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def index(request):
  return render(request, 'index.html')

def home(request):
  drinks = Drink.objects.filter(user=request.user)
  return render(request, 'home.html', {'drinks': drinks})


class DrinkCreate(CreateView):
  model = Drink
  fields = ['name', 'category', 'description', 'rating', 'price']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


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
