from django.contrib import admin

from .models import Floor, Room, Tag, Starter, Main, Dessert, Order


admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Tag)
admin.site.register(Starter)
admin.site.register(Main)
admin.site.register(Dessert)
admin.site.register(Order)
