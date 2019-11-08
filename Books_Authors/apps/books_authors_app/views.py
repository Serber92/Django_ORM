from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def add_book(request):
  context = {
    'books': Book.objects.all()
  }
  return render(request, 'books_authors_app/add_book.html', context)

def add_book_process(request):
  title = request.GET['title']
  description = request.GET['description']
  Book.objects.create(title=title, description=description)
  return redirect('/')

def add_book_description(request, id):
  context = {
    'book': Book.objects.get(id=id),
    'authors': Book.objects.get(id=id).authors.all(),
    'all_authors': Author.objects.all(),
  }
  return render(request, 'books_authors_app/book_description.html', context)

def book_description_process(request, book_id):
  selected_author_id = request.GET['add_author']
  Author.objects.get(id=selected_author_id).books.add(Book.objects.get(id=book_id))
  return redirect('/books/' + book_id)
