from django.db import models
import re, bcrypt
from datetime import datetime, date


class UserManager(models.Manager):
  def registartion_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
      errors['first_name'] = 'First and last name should be at least 2 characters long'
    if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
      errors['first_name'] = 'Name should contain only letters'
    if datetime.strptime(postData['birthday'], '%Y-%m-%d') > datetime.today():
      errors['birthday'] = 'Your birthday cant be a fututre date'
    # *******************checking age*************************
    def calculateAge(birthDate):
      today = date.today()
      age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
      return age
    if calculateAge(datetime.strptime(postData['birthday'], '%Y-%m-%d')) < 13:
      errors['birthday'] = 'Age should be older than 13'
    # *******************checking age*************************
    if not EMAIL_REGEX.match(postData['email']):          
      errors['email'] = "Invalid email address!"
    if len(postData['password']) < 8:
      errors['password'] = 'Password should be at least 8 characters long'
    if postData['password'] != postData['confirm_password']:
      errors['password'] = 'Provided passwords do not match'
    if len(User.objects.filter(email=postData['email'])) != 0:
      errors['email'] = 'This email is already registered'
    return errors
  def login_validator(self, postData):
    errors = {}
    if len(User.objects.filter(email=postData['email'])) == 0:
      errors['email'] = 'This email is not registered'
    elif not bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()):
      errors['password'] = 'Incorrect password'
    return errors


class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  birthday = models.DateTimeField(default=datetime.now)
  email = models.CharField(max_length=45)
  password = models.CharField(max_length=65)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
  def __repr__(self):
    return f"{self.email} {self.password}"


class Message(models.Model):
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user_id = models.ForeignKey(User, related_name="messages")


class Comment(models.Model):
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  message_id = models.ForeignKey(Message, related_name="comments")
  user_id = models.ForeignKey(User, related_name="comments")
