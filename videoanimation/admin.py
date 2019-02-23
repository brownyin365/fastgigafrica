from django.contrib import admin
from . models import Category, Sub_Category, PostVideo, ReviewVideo


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.
admin.site.register(Category, UserProfileAdmin)
admin.site.register(Sub_Category)
admin.site.register(PostVideo)
admin.site.register(ReviewVideo)





admin.site.site_header = 'Administration'


