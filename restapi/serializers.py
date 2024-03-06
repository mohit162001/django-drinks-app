from rest_framework import serializers

from restapi.models import DrinkModel

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkModel
        fields = ['id','name','desc','price','category']