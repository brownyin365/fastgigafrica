from django.contrib import admin
from . models import Category, Sub_Category, Posttech, Reviewtech


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.
admin.site.register(Category, UserProfileAdmin)
admin.site.register(Sub_Category)
admin.site.register(Posttech)
admin.site.register(Reviewtech)





admin.site.site_header = 'Administration'


