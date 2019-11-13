from django.db import models
import re

class UserManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
      errors['first_name'] = 'First and last name should be at least 2 characters long'
    if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
      errors['first_name'] = 'Name should contain only letters'
    if not EMAIL_REGEX.match(postData['email']):          
      errors['email'] = "Invalid email address!"
    if len(postData['password']) < 8:
      errors['password'] = 'Password should be at least 8 characters long'
    if postData['password'] != postData['confirm_password']:
      errors['password'] = 'Provided passwords do not match'
    return errors


class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.CharField(max_length=45)
  password = models.CharField(max_length=65)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()



    