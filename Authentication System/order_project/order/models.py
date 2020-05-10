from django.db import models


class Floor(models.Model):
    floor_num     = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.floor_num)


class Room(models.Model):
    floor         = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_num      = models.PositiveSmallIntegerField(unique=True)
    num_guest     = models.PositiveSmallIntegerField(default=1)

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


class Starter(models.Model):
    starter_name  = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tags          = models.ManyToManyField(Tag)
    show_date     = models.DateField(null=True)

    def __str__(self):
        return self.starter_name


class Main(models.Model):
    main_name     = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tags          = models.ManyToManyField(Tag)
    show_date     = models.DateField(null=True)

    def __str__(self):
        return self.main_name


class Dessert(models.Model):
    dessert_name  = models.CharField(max_length=100, null=True, blank=True)
    date_created  = models.DateTimeField(auto_now_add=True, null=True)
    tags          = models.ManyToManyField(Tag)
    show_date     = models.DateField(null=True)

    def __str__(self):
        return self.dessert_name


class Order(models.Model):
    ORDER_STATUS  = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
    )
    room          = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL)
    starter       = models.ForeignKey(Starter, null=True, on_delete=models.SET_NULL)
    main          = models.ForeignKey(Main, null=True, on_delete=models.SET_NULL)
    dessert       = models.ForeignKey(Dessert, null=True, on_delete=models.SET_NULL)
    ordered_date  = models.DateTimeField(auto_now_add=True, null=True)
    updated_date  = models.DateTimeField(auto_now=True, null=True)
    delivery_time = models.DateTimeField(blank=True)
    status        = models.CharField(max_length=20, choices=ORDER_STATUS, null=True)
