from django.urls import path

from restapi.views import  Drink_create, Drink_delelte, Drink_details, Drinks_view, Login_view, SignUp_view, logoutAction
urlpatterns = [
    path('',Login_view.as_view(),name="/"),
    path('signup',SignUp_view.as_view(),name='signup'),
    path('logout',logoutAction,name="logout"),
    path('drinks',Drinks_view.as_view(),name="drinks"),
    path('drinks/<int:id>',Drink_details.as_view()),
    path('add-drink',Drink_create.as_view(),name='add-drink'),
    path('delete/<int:id>',Drink_delelte)
]
