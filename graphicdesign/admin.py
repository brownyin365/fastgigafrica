from django.contrib import admin
from . models import Category, Sub_Category, GraphicPost, Confirm, Review_Design


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.
admin.site.register(Category, UserProfileAdmin)
admin.site.register(Sub_Category)
admin.site.register(GraphicPost)
admin.site.register(Confirm)
admin.site.register(Review_Design)





admin.site.site_header = 'Administration'

