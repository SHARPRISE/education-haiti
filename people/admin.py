from django.contrib import admin

from people.models import User, Mentor, ToDo
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields          = ('username','email', 'is_staff', 'last_login','undergrad_college')
    list_display    = ('username','email', 'is_staff', 'last_login', 'undergrad_college')
    list_filter     = ('is_staff',)
    date_hierarchy  = 'last_login'
    ordering        = ('username', 'is_staff',)
    search_fields   = ('email', 'username',)


class MentorAdmin(admin.ModelAdmin):
    fields          = ('user','first_name','last_name','undergrad_college','grad_college','majors','interests','residency',
                       'phone','current_status','school_haiti', 'picture')
    list_display = ('first_name', 'last_name', 'undergrad_college', 'majors')
    ordering = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class ToDoAdmin(admin.ModelAdmin):
    fields = ('subject', 'completion')


admin.site.register(User, UserAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(ToDo, ToDoAdmin)
