from django.db import models
from django.contrib.auth.models import User
from django import forms
from dramapp import managers
import datetime
from django.db.models import Sum

# Create your models here.

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # These fields are optional
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


class Rating(models.Model):
    RATING_1 = 1
    RATING_2 = 2
    RATING_3 = 3
    RATING_4 = 4
    RATING_5 = 5
    RATING_CHOICES = ((RATING_1, '1 Star'),
                      (RATING_2, '2 Stars'),
                      (RATING_3, '3 Stars'),
                      (RATING_4, '4 Stars'),
                      (RATING_5, '5 Stars'))
    whisky = models.ForeignKey(Whisky)
    user = models.ForeignKey(User, related_name='dramapp_rating')
    rating = models.IntegerField(choices=RATING_CHOICES)
    date = models.DateTimeField()
    
    def __unicode__(self):
        return "%s rating %s (%s)" % (self.user, self.whisky, self.get_rating_display())
    
    def save(self):
        if not self.id:
            self.date = datetime.datetime.now()
        super(Rating, self).save()
    
    def get_score(self):
        return self.rating_set.aggregate(Sum('rating'))



class Search(models.Model):
    query = forms.CharField(max_length=30, required=False)


