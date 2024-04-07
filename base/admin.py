from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Messege

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Messege)