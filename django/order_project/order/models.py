from django.db import models
from django_currentuser.db.models import CurrentUserField


class Floor(models.Model):
    floor_num     = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.floor_num)


ROOM_STATUS  = (
    ('OCC', 'Occupied'),
    ('CO', 'Check Out'),
    ('V', 'Vacant'),

)


class Room(models.Model):
    floor         = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_num      = models.PositiveSmallIntegerField(unique=True)
    adult         = models.PositiveSmallIntegerField(default=1)
    kid           = models.PositiveSmallIntegerField(default=0)
    status        = models.CharField(max_length=20, choices=ROOM_STATUS, default='Vacant')

    def __str__(self):
        return str(self.room_num)


    def save_model(self, request, obj, form, change):
        if not change:
            account = Account.objects.get(email=request.user)
            obj.floor = account.floors.all().first()
        obj.save()


class Tag(models.Model):
    tag_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.tag_name



DAYS = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)



class Starter(models.Model):
    starter_name  = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tags          = models.ManyToManyField(Tag)
    day           = models.CharField(max_length=3, choices=DAYS, null=True)

    def __str__(self):
        return self.starter_name


class Main(models.Model):
    main_name     = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tags          = models.ManyToManyField(Tag)
    day           = models.CharField(max_length=3, choices=DAYS, null=True)

    def __str__(self):
        return self.main_name


class Dessert(models.Model):
    dessert_name  = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tags          = models.ManyToManyField(Tag)
    day           = models.CharField(max_length=3, choices=DAYS, null=True)
    
    def __str__(self):
        return self.dessert_name


ORDER_STATUS  = (
    ('pending', 'Pending'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),

)


class BreakfastOrder(models.Model):
    user          = CurrentUserField()
    room          = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    is_needed     = models.BooleanField(default=False, null=True)
    ordered_date  = models.DateTimeField(auto_now_add=True, null=True)
    updated_date  = models.DateTimeField(auto_now=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    comment       = models.CharField(max_length=200, blank=True, null=True)
    status        = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')

    def __str__(self):
        return str(self.room)


class LunchOrder(models.Model):
    user          = CurrentUserField()
    room          = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    starter       = models.ForeignKey(Starter, blank=True, null=True, on_delete=models.SET_NULL)
    main          = models.ForeignKey(Main, blank=True, null=True, on_delete=models.SET_NULL)
    dessert       = models.ForeignKey(Dessert, blank=True, null=True, on_delete=models.SET_NULL)
    ordered_date  = models.DateTimeField(auto_now_add=True, null=True)
    updated_date  = models.DateTimeField(auto_now=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    comment       = models.CharField(max_length=200, blank=True, null=True)
    status        = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')

    def __str__(self):
        return str(self.room)


class DinnerOrder(models.Model):
    user          = CurrentUserField()
    room          = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    starter       = models.ForeignKey(Starter, blank=True, null=True, on_delete=models.SET_NULL)
    main          = models.ForeignKey(Main, blank=True, null=True, on_delete=models.SET_NULL)
    dessert       = models.ForeignKey(Dessert, blank=True, null=True, on_delete=models.SET_NULL)
    ordered_date  = models.DateTimeField(auto_now_add=True, null=True)
    updated_date  = models.DateTimeField(auto_now=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    comment       = models.CharField(max_length=200, blank=True, null=True)
    status        = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')

    def __str__(self):
        return str(self.room)
