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
    def resolve_drinks(root,info):
        return DrinkModel.objects.all()
    
    
    drink = graphene.Field(DrinkType,id=graphene.String())
    def resolve_drink(root,info,id):
        return DrinkModel.objects.get(id=id)
    
    
    categories = graphene.List(CategoryType)
    def resolve_categories(root,info):
        print(info.operation)
        print(root)
        return CategoryModel.objects.all()
    
    
    category = graphene.Field(CategoryType,id=graphene.String())
    def resolve_category(root,info,id):
        return CategoryModel.objects.get(id=id)
      

class DrinkCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        desc = graphene.String(required=True)
        category_id = graphene.String(required=True)
    
    drink = graphene.Field(DrinkType)
    
    @classmethod
    def mutate(cls,root,info,name,desc,price,category_id):
        category = CategoryModel.objects.get(id=category_id)
        drink = DrinkModel.objects.create(name=name,desc=desc,price=price,category=category)
        drink.save()
        return DrinkCreate(drink)


class DrinkUpdate(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        desc = graphene.String()
        price = graphene.Float()
        id = graphene.ID(required=True)
        
    drink = graphene.Field(DrinkType)

    @classmethod
    def mutate(cls,root,info,id,name,desc,price):
        drink = DrinkModel.objects.get(id=id)
        drink.name = name
        drink.desc = desc
        drink.price = price
        drink.save()
        return DrinkUpdate(drink)
    
    
class DrinkDelete(graphene.Mutation):
    class Arguments:
        id = graphene.String(required = True)
        
    message = graphene.String()
    
    @classmethod
    def mutate(cls,root,info,id):
   
        drink = DrinkModel.objects.get(id=id)
        drink.delete()
        return DrinkDelete(message = "Drink delelted successfully")
    
    
class Mutation(graphene.ObjectType):
    update_drink = DrinkUpdate.Field()
    create_drink = DrinkCreate.Field()
    delete_drink = DrinkDelete.Field()
    
        
schema = graphene.Schema(query=Query,mutation=Mutation)