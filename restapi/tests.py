from venv import create
from django.test import TestCase
from django.contrib.auth.models import User
from restapi.models import DrinkModel
from graphene_django.utils.testing import GraphQLTestCase
# Create your tests here.

# class TestViews(TestCase):
#     def setUp(self):
#         User.objects.create_user("test123","test123@gmail.com","test123")
#         self.client.login(username="test123",password="test123")
    
#     def test_drink(self):
#         drink = DrinkModel.objects.create(name="chai",desc="hot drink mixed with tea leafs and sugar with milk",price=20)
#         print(drink)
#         self.assertEqual(drink.name,"chai")

class TestDrinkQuery(GraphQLTestCase):
    def test_drink_query(self):
        self.drink = DrinkModel.objects.create(id=11, name="Grape juice", desc="Its a juice of grape")
        expected = {
            "data": {
                "drink": {
                    "name": "Grape juice",
                    "desc": "Its a juice of grape"
                    }
                }
            }
        
        res = self.query("""
                    {
                        drink(id:"11"){
                            name
                            desc
                         }
                    }
                """)
        print("---------------------------------------",res.json())
        self.assertEqual(expected,res.json())
        
        