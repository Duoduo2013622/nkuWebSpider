from django.contrib import admin
from .models import *

# Register your models here.

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','url', 'pub_date']

admin.site.register(NewsInfo,NewsInfoAdmin)