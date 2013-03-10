from django.contrib import admin
from dramapp.models import Region, Distillery, Whisky#, Comments
from dramapp.models import UserProfile

admin.site.register(Region)
admin.site.register(Distillery)
admin.site.register(Whisky)
#admin.site.register(Comments)
admin.site.register(UserProfile)

