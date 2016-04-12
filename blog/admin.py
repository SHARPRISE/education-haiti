from django.contrib import admin
from .models import SuccessStory

# Register your models here.


class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ['title','description','author']
    list_filter = ['created']
    search_fields = ['title','description','content']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(SuccessStory, SuccessStoryAdmin)