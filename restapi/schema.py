import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import CategoryModel, DrinkModel

class DrinkType(DjangoObjectType):
    class Meta:
        model = DrinkModel
        fields = '__all__'

class CategoryType(DjangoObjectType):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class Query(ObjectType):
    
    drinks = graphene.List(DrinkType)
    def resolve_drinks(root,info):
        return DrinkModel.objects.all()
    
    drink = graphene.Field(DrinkType,id=graphene.String())
    def resolve_drink(root,info,id):
        return DrinkModel.objects.get(id=id)
    
    categories = graphene.List(CategoryType)
    def resolve_categories(root,info):
        return CategoryModel.objects.all()
    
    category = graphene.Field(CategoryType,id=graphene.String())
    def resolve_category(root,info,id):
        return CategoryModel.objects.get(id=id)
    
 
schema = graphene.Schema(query=Query)