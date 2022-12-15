from django.contrib import admin
from .models import FM

class FMAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'image1', 'image2', 'image3', 'image4', 'image5', 'slug', 'is_pub']
    list_editable = ['title', 'desc', 'image1', 'image2', 'image3', 'image4', 'image5', 'slug', 'is_pub']

admin.site.register(FM, FMAdmin)
