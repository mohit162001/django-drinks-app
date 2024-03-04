from django.http import JsonResponse
from django.shortcuts import redirect, render
from restapi.forms import DrinkForm
from restapi.models import DrinkModel
from restapi.serializers import DrinkSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class Drinks_view(APIView):
    def get(self, request):
        drinks = DrinkModel.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return render(request,'drinks.html',{"drinks":serializer.data})


class Drink_create(APIView):
 
    permission_classes = [IsAuthenticated]
    def get(self,request):
        form = DrinkForm()
        return render(request,'add_drink.html',{"form":form})
    
    def post(self, request):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("http://localhost:8080/drinks")
        
           

class Drink_details(APIView):
    def get_drink(self, id):
        try:
            return DrinkModel.objects.get(id=id)
        except:
            return None

    def get(self, request, id):
        drink = self.get_drink(id)
        if drink is not None:
            serializer = DrinkSerializer(drink)
            return render(request,'drink_details.html',{"drink":serializer.data})
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
        
    def delete(self,request,id):
        drink = self.get_drink(id)
        if drink is not None:
            drink.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error":"Cant not delete"},status=status.HTTP_400_BAD_REQUEST)

