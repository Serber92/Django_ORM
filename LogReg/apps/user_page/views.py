from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
  return render(request, 'user_page/index.html')

def registration(request):
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password']
  confirm_password = request.POST['confirm_password']

  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
      return redirect('/')
  else:
    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    return redirect('/success')


def login(request):
  email = request.POST['email']
  password = request.POST['password']

  
  return redirect('/success')

def success(request):
  context = {
    'name': User.objects.last().first_name,
  }
  return render(request, 'user_page/success.html', context)

