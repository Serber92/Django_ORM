from django.db import models

class First_class(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
      return f"<First_class object: {self.title} ({self.id})>"


class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email_adress = models.CharField(max_length=255)
  age = models.IntegerField()
  created_at = models.DateField(auto_now=False, auto_now_add=True)
  updated_at = models.DateField(auto_now=True, auto_now_add=False)
