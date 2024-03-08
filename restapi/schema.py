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
    
    # filter_drinks_by_desc = graphene.List(DrinkType,search = graphene.String())
    # def resolve_filter_drinks_by_desc(root,info,search):        
    #     return DrinkModel.objects.filter(desc__icontains = search)
    
    
    # filter_drinks_by_name = graphene.List(DrinkType,name = graphene.String())
    # def resolve_filter_drinks_by_name(root,info,name):        
    #     return DrinkModel.objects.filter(name__istartswith = name)
    
    
    # filter_drinks_by_price = graphene.List(DrinkType,price = graphene.Float())
    # def resolve_filter_drinks_by_price(root,info,price): 
    #     return DrinkModel.objects.filter(price__exact = price)
    
    # filter_drink = graphene.List(DrinkType,name=graphene.String(),desc=graphene.String(),price=graphene.Float())
    # def resolve_filter_drink(root,info,name=None,desc=None,price=None):
    #     if name or desc or price:

    #         return DrinkModel.objects.filter(desc__icontains = desc) | DrinkModel.objects.filter(name__istartswith = name) |DrinkModel.objects.filter(price__exact = price)
    
    filter_drink = graphene.List(DrinkType, name=graphene.String(), desc=graphene.String(), price=graphene.Float())

    def resolve_filter_drink(root, info, name=None, desc=None, price=None):
        drinks = DrinkModel.objects.all()

        if name:
            drinks = drinks.filter(name__istartswith=name)
        if desc:
            drinks = drinks.filter(desc__icontains=desc)
        if price is not None:
            drinks = drinks.filter(price=price)

        return drinks

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
    def mutate(cls,root,info,id,name=None,desc=None,price=None):
        if name is not None:
            DrinkModel.objects.filter(id=id).update(name=name)
        if price is not None:
            DrinkModel.objects.filter(id=id).update(price=price)
        if desc is not None:
            DrinkModel.objects.filter(id=id).update(desc=desc)
            
        update_drink = DrinkModel.objects.get(id=id)
        return DrinkUpdate(update_drink)
    
    
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