from django.contrib import admin
from . models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'mobileConfirm', 'chips', 'staff', 'admin')
    list_filter = ('mobileConfirm', 'staff')

