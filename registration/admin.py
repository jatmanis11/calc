from django.contrib import admin
from registration.models import user_data

class useradmin(admin.ModelAdmin):
    list_display=("user_name", "user_mobile", "user_email")

admin.site.register(user_data, useradmin)
# Register your models here.
