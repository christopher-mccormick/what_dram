from django.contrib import admin
from dramapp.models import Region, Distillery, Whisky, UserProfile
from ratings import models

admin.site.register(Region)
admin.site.register(Distillery)
admin.site.register(Whisky)
admin.site.register(UserProfile)


