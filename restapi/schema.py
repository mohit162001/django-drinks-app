import graphene
from graphene_django import DjangoObjectType
from .models import DrinkModel

class DrinkType(DjangoObjectType):
    class Meta:
        model = DrinkModel
        fields = '__all__'

class Query(graphene.ObjectType):
    drinks = graphene.List(DrinkType)
    drink = graphene.Field(DrinkType,id=graphene.String())
    
    def resolve_drinks(root,info):
        return DrinkModel.objects.all()
    
    def resolve_drink(root,info,id):
        return DrinkModel.objects.get(id=id)
    
schema = graphene.Schema(query=Query)