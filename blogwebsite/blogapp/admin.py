from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import BlogPost,Category, Tags
# Register your models here.



class MainAppAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'published_date']
    list_display_links= ['id','title',]

admin.site.register(BlogPost,  MainAppAdmin)
admin.site.register(Category)
admin.site.register(Tags)

admin.site.site_header='Django Blog Website Panel'
admin.site.site_title= "Site portal"
admin.site.index_title= "Site Administrative Panel"