from django.contrib import admin
from .models import *
from django_google_maps import fields as map_fields

# Register your models here.
admin.site.register(User)
admin.site.register(Location)


