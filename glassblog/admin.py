from django.contrib import admin
from .models import BlogPost



# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    
admin.site.register(BlogPost, BlogPostAdmin)