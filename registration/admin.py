from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount, Profile,RequestForSuperUserPrivileges

# Register your models here.
@admin.register(UserAccount)
class MyUserAdmin(UserAdmin):
        model = UserAccount
        list_display = ('username','User_Type',
                        'email')
        list_filter = ('username',
                        'email','User_Type')
        search_fields = ('username','email' )
        ordering = ('username','email' )


@admin.register(RequestForSuperUserPrivileges)
class MyUserPrivilegeAdmin(admin.ModelAdmin):
        model = RequestForSuperUserPrivileges
        list_display = ('username',
                        'email','Request_For_SuperUser')
        list_filter = ('username',
                        'email')
        ordering = ('username','email' )