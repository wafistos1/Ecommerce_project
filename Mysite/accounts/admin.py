from django.contrib import admin
from accounts.models import Profile


admin.site.site_header = 'Admin Yatach'  # Change page title
admin.site.register(Profile)  # delete group

# Register your models here.
