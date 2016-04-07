from django.contrib import admin

from people.models import User, Profile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields          = ('email', 'username', 'is_staff', 'last_login',)
    list_display    = ('email', 'username', 'is_staff', 'last_login',)
    list_filter     = ('is_staff',)
    date_hierarchy  = 'last_login'
    ordering        = ('email', 'is_staff',)
    search_fields   = ('email', 'username',)

class ProfileAdmin(admin.ModelAdmin):
    fields          = ('user',)

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
