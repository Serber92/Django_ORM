from django.shortcuts import render, redirect
from .models import Shows
from django.contrib import messages

def shows(request):
  context = {
    'all_shows': Shows.objects.all()
  }
  return render(request, 'first_app/shows.html', context)

def new(request):
  return render(request, 'first_app/shows_new.html')

def new_process(request):
  errors = Shows.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
      return redirect('/shows/new')
  else:
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']
    Shows.objects.create(title=title, network=network, release_date=release_date, description=description)
    show_id = Shows.objects.last().id
    return redirect('/shows/' + str(show_id))

def shows_info(request, show_index):
  context = {
    "show_index" : show_index,
    "show": Shows.objects.get(id=show_index)
  }
  return render(request, 'first_app/shows_info.html', context)

def delete(request, show_id):
  Shows.objects.filter(id=show_id).delete()
  return redirect('/shows')

def edit(request, show_id):
  context = {
    'show_id' : show_id,
    'show' : Shows.objects.get(id=show_id),
  }
  return render(request, 'first_app/edit.html', context)

def edit_process(request):
  title = request.POST['title_edit'] 
  show_id = Shows.objects.filter(title=title)[0].id
  network = request.POST['network_edit']  
  release_date = request.POST['release_date_edit']
  description = request.POST['description_edit']
  Shows.objects.filter(id=show_id).update(title=title, network=network, release_date=release_date, description=description)
  return redirect('/shows/' + str(show_id))

