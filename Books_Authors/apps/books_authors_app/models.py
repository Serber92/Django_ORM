from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  def __repr__(self):
    return f"{self.title}"


class Author(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
  updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  books = models.ManyToManyField(Book, related_name='authors')
  notes = models.TextField(default='no notes')
  def __repr__(self):
    return f"{self.first_name} {self.last_name}"