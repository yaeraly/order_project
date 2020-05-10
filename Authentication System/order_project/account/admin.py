from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'username', 'first_name', 'last_name', 'last_login', 'is_admin',
        'is_active', 'is_staff', 'is_superuser',
    )
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
