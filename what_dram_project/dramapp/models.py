from django.db import models
from django.contrib.auth.models import User
from django import forms
from dramapp import managers
import datetime
from django.db.models import Sum

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()


    def __unicode__(self):
        return self.user.username


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth']


class Region(models.Model):
    region = models.CharField(max_length=30)

    def __unicode__(self):
        return self.region


class Distillery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region)
    latitude = models.FloatField()
    longitude = models.FloatField()
    images = models.URLField()
    website = models.URLField()
    tourevents = models.CharField(max_length=200)
    blurb = models.CharField(max_length=10000)

    def __unicode__(self):
        return self.name


class Whisky(models.Model):
    objects = managers.WhiskyManager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    whiskytype = models.CharField(max_length=30)
    distillery = models.ForeignKey(Distillery)
    region = models.ForeignKey(Region)
    tastingnotes = models.CharField(max_length=200)
    barrelType = models.CharField(max_length=30)
    image = models.URLField()
    website = models.URLField()
    price = models.FloatField()

    def __unicode__(self):
        return self.name

class Search(models.Model):
    query = forms.CharField(max_length=30, required=False)
