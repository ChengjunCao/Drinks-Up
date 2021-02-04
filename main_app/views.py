from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from .models import Drink
from .forms import DrinkForm
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'albumcollector'


def main(request):
  return render(request, 'main.html')

def home(request):
  drinks = Drink.objects.filter(user=request.user)[:3]
  return render(request, 'home.html', {'drinks': drinks})

def drinks_index(request):
  drinks = Drink.objects.filter(user=request.user)
  return render(request, 'drinks/index.html', {'drinks': drinks})

def drinks_detail(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  return render(request, 'drinks/detail.html', {'drink': drink})

def create_page(request):
  drink_form = DrinkForm()
  return render(request, 'main_app/drink_form.html', {'drink_form': drink_form})

def create_drink(request):
  image_file = request.FILES.get('image-file', None)
  if image_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + image_file.name[image_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(image_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      print(request.POST)
      drink = Drink(url=url, name=request.POST['name'], location=request.POST['location'], price=request.POST['price'],
                    type=request.POST['type'], rating=request.POST['rating'], description=request.POST['description'], user=request.user)
      drink.save()
      return redirect('detail', drink_id=drink.id)
    except:
      print('An error occurred uploading file to S3')
  

def update_page(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  return render(request, 'drinks/update.html', {'drink': drink})

def update_drink(request, drink_id):
  drink = Drink.objects.get(id=drink_id)
  drink.user = request.user
  drink.name = request.POST['name']
  drink.location = request.POST['location']
  drink.price = request.POST['price']
  drink.type = request.POST['type']
  drink.rating = request.POST['rating']
  drink.description = request.POST['description']
  drink.save()
  return redirect('detail', drink_id=drink_id)


# class DrinkUpdate(UpdateView):
#   model = Drink
#   fields = ['type', 'price', 'description']

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

def search_page(request):
  return render(request, 'drinks/search_page.html')

def search_result(request):
  search = request.POST['drink_name']
  # print('Searching for', search)
  results = Drink.objects.filter(name__contains=search)
  # print (results)
  return render(request, 'drinks/result.html', {'results': results})

  