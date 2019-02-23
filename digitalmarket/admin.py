from django.contrib import admin
from . models import Category, Sub_Category, Confirm, Postdigit, Reviewdigit


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['name']

# Register your models here.
admin.site.register(Category, UserProfileAdmin)
admin.site.register(Sub_Category)
admin.site.register(Postdigit)
admin.site.register(Confirm)
admin.site.register(Reviewdigit)





admin.site.site_header = 'Administration'


