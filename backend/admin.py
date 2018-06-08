from django.contrib import admin
from .models import MenuEntry, Room, User
# Register your models here.
admin.site.register(Room)
admin.site.register(MenuEntry)
admin.site.register(User)
