from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from restapi.forms import DrinkForm
from restapi.models import CategoryModel, DrinkModel
from restapi.serializers import DrinkSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUp_view(APIView):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if not (username and email and password):
            return HttpResponse("fill all fields")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/')
    


class Login_view(APIView):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('drinks')
        else:
            return HttpResponse("something went wrong...!\n Unable to login")

def logoutAction(request):
    logout(request)
    return redirect('/')

class Drinks_view(LoginRequiredMixin,APIView):
    login_url = '/'
    def get(self, request):
        drinks = DrinkModel.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return render(request,'drinks.html',{"drinks":serializer.data})
        # return Response(serializer.data)

class Drink_create(LoginRequiredMixin,APIView):
    login_url = '/'
    def get(self,request):
        categories = CategoryModel.objects.all()
        return render(request,'add_drink.html',{"categories":categories})
    
    def post(self, request):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("http://localhost:8080/drinks")
        
           
class Drink_details(LoginRequiredMixin,APIView):
    login_url = '/'
    def get_drink(self, id):
        try:
            return DrinkModel.objects.get(id=id)
        except:
            return None

    def get(self, request, id):
        drink = self.get_drink(id)
        if drink is not None:
            return render(request,'drink_details.html',{"drink":drink})
        else:
            return Response({"error":"soemthing went wrong"})
        
    def put(self,request,id):
        drink = self.get_drink(id)
        if drink is not None:
            serializer = DrinkSerializer(drink,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"soemthing went wrong"})
        
def Drink_delelte(request,id):
    drink = DrinkModel.objects.get(pk=id)
    if drink is not None:
        drink.delete()
        return redirect('drinks')
    else:
        return Response({"error":"Cant not delete"},status=status.HTTP_400_BAD_REQUEST)
    


