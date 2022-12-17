from django.contrib import admin
from .models import FM, Vacancy

class FMAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','images_count', 'is_pub'] 
    search_fields = ['id', 'title', ] 
    list_editable = ['is_pub', 'price']
    actions = ['set_pub', 'delete_desc', 'delete_photos']

    @admin.action(description='Publish')
    def set_pub(self, request, qs):
        qs.update(is_pub=True)
        self.message_user(request, 'Post Published')

    @admin.action(description='Delete Description')
    def delete_desc(self, request, qs):
        qs.update(desc='')
        self.message_user(request, 'All Descriptions Removed')

    @admin.action(description='Delete All Photos')
    def delete_photos(self,request,qs):
        qs.update(image1 = '', image2 = '', image3 = '', image4 = '', image5 = '')
        self.message_user(request, 'Photos Removed')

admin.site.register(FM, FMAdmin)
admin.site.register(Vacancy)
