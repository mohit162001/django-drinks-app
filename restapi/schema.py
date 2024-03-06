import graphene
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

class Query(graphene.ObjectType):
    drinks = graphene.List(DrinkType)
    drink = graphene.Field(DrinkType,id=graphene.String())
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType,id=graphene.String())
    
    def resolve_drinks(root,info):
        return DrinkModel.objects.all()
    
    def resolve_drink(root,info,id):
        return DrinkModel.objects.get(id=id)
    
    def resolve_categories(root,info):
        return CategoryModel.objects.all()
    
    def resolve_category(root,info,id):
        return CategoryModel.objects.get(id=id)
    
    
schema = graphene.Schema(query=Query)