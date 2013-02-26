from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
#from ratings.handlers import ratings


# Create your models here.

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # These fields are optional
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
	name = models.CharField(max_length=30)
	region = models.ForeignKey(Region)
	longitude = models.IntegerField()
	latitude = models.IntegerField()
	images = models.URLField()
	website = models.URLField()
	tourevents = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Whisky(models.Model):
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	whiskytype = models.CharField(max_length=30)
	distillery = models.ForeignKey(Distillery)
	region = models.ForeignKey(Region)
	rating = models.FloatField()
	tastingnotes = models.CharField(max_length=200)
	barrelType = models.CharField(max_length=30)
	image = models.URLField()
	website = models.URLField()
	price = models.FloatField()

	def __unicode__(self):
		return self.name


class Comments(models.Model):
	comments = models.CharField(max_length=400)
	name = models.ForeignKey(Whisky)
	user = models.ForeignKey(UserProfile)

	def __unicode__(self):
		return self.comments

#ratings.register(Whisky)






