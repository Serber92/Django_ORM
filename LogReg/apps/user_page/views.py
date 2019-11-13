from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request, log_reg=''):
  context = {
    'log_reg': log_reg
  }
  return render(request, 'user_page/index.html', context)

def registration(request):
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  birthday = request.POST['birthday']
  email = request.POST['email']
  hash_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

  errors = User.objects.registartion_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
      return redirect('/')
  else:
    User.objects.create(first_name=first_name, last_name=last_name, birthday=birthday, email=email, password=hash_password)
    request.session['user_id'] = User.objects.get(email=email).id
    return redirect('/success')


def login(request):
  email = request.POST['email']
  errors = User.objects.login_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
      return redirect('/')
  else:
    request.session['user_id'] = User.objects.get(email=email).id
    return redirect('/success')

def success(request):
  context = {
    'name': User.objects.get(id=request.session['user_id']).first_name,
  }
  return render(request, 'user_page/success.html', context)

def logout(request):
  request.session.flush()
  return redirect('/')

