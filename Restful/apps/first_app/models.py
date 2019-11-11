from django.db import models
from django import forms


class Shows(models.Model):
  title = models.CharField(max_length=25)
  network = models.CharField(max_length=25)
  release_date = models.DateField()
  description = models.TextField(default='No description')
  def __repr__(self):
    return f"{self.title} {self.network}"
