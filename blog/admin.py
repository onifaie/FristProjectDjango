from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    mydate=date.day
    list_display = ['title', 'dateAdd', 'user','discrption']
    list_filter=['title','dateAdd']
    search_fields=['title','discrption']

