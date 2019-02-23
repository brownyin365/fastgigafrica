from django.contrib import admin
from . models import UserProfile, Profile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user','location','skill','phone','website','education','bio','photo']

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Profile, UserProfileAdmin)




admin.site.site_header = 'Administration'

