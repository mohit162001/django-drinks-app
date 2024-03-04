from venv import create
from django.test import TestCase
from django.contrib.auth.models import User
from restapi.models import DrinkModel
# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        User.objects.create_user("test123","test123@gmail.com","test123")
        self.client.login(username="test123",password="test123")
    
    def test_drink(self):
        drink = DrinkModel.objects.create(name="chai",desc="hot drink mixed with tea leafs and sugar with milk",price=20)
        print(drink)
        self.assertEqual(drink.name,"chai")