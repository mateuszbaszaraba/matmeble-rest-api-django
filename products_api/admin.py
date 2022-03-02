from django.contrib import admin
from . import models


@admin.register(models.Product)
class Products(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')


admin.site.register(models.SoftFurniture)
admin.site.register(models.Armchair)
