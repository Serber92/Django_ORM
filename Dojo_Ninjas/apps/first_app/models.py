from django.db import models

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=2)
  description = models.TextField(default='This is default description of Dojo')

class Ninja(models.Model):
  dojo = models.ForeignKey(Dojo, related_name='ninjas')
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
