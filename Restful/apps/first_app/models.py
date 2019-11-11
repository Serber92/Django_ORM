from django.db import models
from django import forms
import re, datetime

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        DATE_REGEX = re.compile(r'^[0-9][0-9][0-9][0-9]+\-[0-9][0-9]+\-[0-9][0-9]$')
        today_date = datetime.datetime.today()
        posted_date = datetime.datetime.strptime(postData['release_date'], '%Y-%m-%d')
        # add keys and values to errors dictionary for each invalid field
        print('**********today:', today_date)
        print('***********posted:', posted_date)
        if len(postData['title']) > 25:
            errors["name"] = "Title name is too long"
        if len(postData['description']) < 10:
            errors["description"] = "Description is too short"
        if not DATE_REGEX.match(postData['release_date']):
          errors['release_date'] = ('Invalid date format')
        if posted_date > today_date:
          errors['release_date'] = ('Date can\'t be in the future')
        return errors

class Shows(models.Model):
  title = models.CharField(max_length=25)
  network = models.CharField(max_length=25)
  release_date = models.DateField()
  description = models.TextField(default='No description')
  objects = ShowsManager()
  def __repr__(self):
    return f"{self.title} {self.network}"

