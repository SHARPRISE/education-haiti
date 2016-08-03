from django.contrib import admin
from .models import Programs
# Register your models here.


class ProgramsAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'description', 'slug', 'details', 'start_date', 'end_date', 'fee',
              'phone_contact', 'email_contact', 'deadline', 'picture')


admin.site.register(Programs, ProgramsAdmin)
