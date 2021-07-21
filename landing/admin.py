from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Table)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(Receipt)

class MenuItemAdmin(admin.ModelAdmin):
    readonly_fields = ('create_timestamp','modify_timestamp',)

admin.site.register(MenuItem, MenuItemAdmin)






