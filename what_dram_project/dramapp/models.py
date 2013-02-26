from django.db import models

# Create your models here.

class Region(models.Model):
	region = models.CharField(max_length=30)

	def_unicode_(self):
			return self.region


class Distillery(models.Model):
	name = models.CharField(max_length=30)
	region = models.ForeignKey(Region)
	longitude = models.IntegerField()
	latitude = models.IntegerField()
	images = models.URLField()
	website = models.URLField()
	tourevents = models.CharField(max_length=200)

	def_unicode_(self):
			return self.name


class Whisky(models.Model):
	name = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	whiskytype = models.CharField(max_length=30)
	distillery = models.ForeignKey(Distillery)
	region = models.ForeignKey(Region)
	rating = models.DoubleField()
	tastingnotes = models.CharField(max_length=200)
	barrelType = models.CharField(max_length=30)
	image = models.URLField()
	website = models.URLField()
	price = models.DoubleField()

	def_unicode_(self):
			return self.name

class Member(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=32, min_length=8)
	dob = models.DateField()

	def_unicode_(self):
		return self.username

class Comments(models.Model):
	comments = models.CharField(max_length=400)
	whiskyname = models.ForeignKey(Whisky)
	username = models.ForeignKey(Member)

	def_unicode_(self):
		return self.comments





