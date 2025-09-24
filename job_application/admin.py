from django.contrib import admin
from .models import Form

class AdminForm(admin.ModelAdmin):
    list_display = ("first_name" , "last_name" , "email" , "phone")
    search_fields = ("first_name" , "last_name" , "email" , "phone")
    list_filter = ("availability"  , "position")
    ordering = ("first_name",)
    readonly_fields = ("position" ,)
    list_display_links = ("first_name" ,)

admin.site.register(Form , AdminForm)
