from django.contrib import admin

from api import models


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(models.Categories, CategoryAdmin)
