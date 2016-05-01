from django.contrib import admin

from people.models import User, Mentor, Mentee
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields          = ('email', 'username', 'is_staff', 'last_login', 'university')
    list_display    = ('email', 'username', 'is_staff', 'last_login', 'university')
    list_filter     = ('is_staff',)
    date_hierarchy  = 'last_login'
    ordering        = ('email', 'is_staff',)
    search_fields   = ('email', 'username',)

class MentorAdmin(admin.ModelAdmin):
    fields          = ('user','university')

class MenteeAdmin(admin.ModelAdmin):
    fields          = ('user',)

admin.site.register(User, UserAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Mentee, MenteeAdmin)
