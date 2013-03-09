from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

# Create your models here

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

#class Rating(models.Model):
#	STAR_1 = 1
#	STAR_2 = 2
#	STAR_3 = 3
#	STAR_4 = 4
#	STAR_5 = 5
#	RATING_CHOICES = ((STAR_1, '1 Star')
#						(STAR_2, '2 Stars')
#						(STAR_3, '3 Stars')
#						(STAR_4, '4 Stars')
#						(STAR_5, '5 Stars'))
#	whisky = models.ForeignKey(Whisky)
#	user = models.ForeignKey(UserProfile)
#	rating = models.IntegerField(choices = RATING_CHOICES)
#	date = models.DateTimeField()

#	def __unicode__(self):
#		return "%s rating %s (%s)" % (self.user, self.whisky, self.get_rating_disply())

#	def save(self):
#		if not self.id:
#			self.date = datetime.datetime.now()
#		super(Rating, self).save()

#	def get_score(self):
#		return sum(self.rating_set.vales('rating', flat = True))

class Distillery(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	region = models.ForeignKey(Region)
	latitude = models.FloatField()
	longitude = models.FloatField()
	images = models.URLField()
	website = models.URLField()
	tourevents = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Whisky(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	whiskytype = models.CharField(max_length=30)
	distillery = models.ForeignKey(Distillery)
	region = models.ForeignKey(Region)
	rating = models.CharField(max_length=5)
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

class Search(models.Model):
  query = forms.CharField(max_length=30, required=False)
