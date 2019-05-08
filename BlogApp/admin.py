from django.contrib import admin
from BlogApp.models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','description','image','upload_date','author']

admin.site.register(Blog,BlogAdmin)
