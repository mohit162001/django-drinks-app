from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class DrinkModel(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 400)
    price = models.FloatField(max_length = 100)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name 

