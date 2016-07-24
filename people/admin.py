from django.contrib import admin

from people.models import User, Mentor, ToDo
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields          = ('email', 'username', 'is_staff', 'last_login','undergrad_college')
    list_display    = ('email', 'username', 'is_staff', 'last_login', 'undergrad_college')
    list_filter     = ('is_staff',)
    date_hierarchy  = 'last_login'
    ordering        = ('email', 'is_staff',)
    search_fields   = ('email', 'username',)


class MentorAdmin(admin.ModelAdmin):
    fields          = ('user','first_name','last_name','biography','undergrad_college','grad_college','majors','interests','residency',
                       'phone','current_status','school_haiti', 'picture')


class ToDoAdmin(admin.ModelAdmin):
    fields = ('subject', 'completion')


admin.site.register(User, UserAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(ToDo, ToDoAdmin)

