from django.contrib import admin

from restapi.models import CategoryModel, DrinkModel

# Register your models here.
admin.site.register(DrinkModel)
admin.site.register(CategoryModel)