from django.contrib import admin

from .models import *
# Register your models here.
from . import models



class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'sex']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 3



admin.site.register(models.Student, BookInfoAdmin)
