from django.contrib import admin

from .models import Floor, Room, Tag, Starter, Main, Dessert, BreakfastOrder, LunchOrder, DinnerOrder
from account.models import Account


class RoomAdmin(admin.ModelAdmin):
    exclude = ['floor']
    def save_model(self, request, obj, form, change):
        if not change:
            account = Account.objects.get(email=request.user)
            obj.floor = account.floors.all().first()
        obj.save()


admin.site.register(Floor)
admin.site.register(Room, RoomAdmin)
admin.site.register(Tag)
admin.site.register(Starter)
admin.site.register(Main)
admin.site.register(Dessert)
admin.site.register(BreakfastOrder)
admin.site.register(LunchOrder)
admin.site.register(DinnerOrder)

