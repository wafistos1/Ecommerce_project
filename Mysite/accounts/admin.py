from django.contrib import admin
from accounts.models import Profile, Adresse
from django.contrib.auth.models import Group


admin.site.site_header = 'Admin Yatach' # Change page title
admin.site.register(Profile)
admin.site.register(Adresse)
admin.site.unregister(Group) # delete group 

# Register your models here.
