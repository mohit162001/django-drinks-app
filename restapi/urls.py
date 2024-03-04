from django.urls import path

from restapi.views import  Drink_create, Drink_details, Drinks_view
urlpatterns = [
    path('drinks',Drinks_view.as_view()),
    path('drinks/<int:id>',Drink_details.as_view()),
    path('add-drink',Drink_create.as_view()),


]
