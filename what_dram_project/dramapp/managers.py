from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class WhiskyManager(models.Manager):
	
    def top_rated(self):
        return self.annotate(score=Sum('rating')).order_by('score')