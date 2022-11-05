from django.contrib import admin
from profiles_api import models

# Register your models here.

#Register our User Profile model with admin sight
admin.site.register(models.UserProfile)