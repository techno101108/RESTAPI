
Drink API
This is a simple Django Rest Framework API for managing a list of drinks.

Endpoints
GET /drinks/
Returns a list of all drinks in the database. Each drink is represented as a JSON object with the following fields:

id: The unique identifier of the drink.
name: The name of the drink.
price: The price of the drink.
Example response:

json
 
[
    {
        "id": 1,
        "name": "Coke",
        "price": "1.50"
    },
    {
        "id": 2,
        "name": "Pepsi",
        "price": "1.50"
    }
]
POST /drinks/
Creates a new drink with the given data. The request body should be a JSON object with the following fields:

name: The name of the drink.
price: The price of the drink.
Example request:

json
 
{
    "name": "Sprite",
    "price": "1.50"
}
Example response:

json
 
{
    "id": 3,
    "name": "Sprite",
    "price": "1.50"
}
GET /drinks/<id>/
Returns the drink with the given ID. The response is a JSON object with the same fields as the GET /drinks/ endpoint.

Example response:

json
 
{
    "id": 1,
    "name": "Coke",
    "price": "1.50"
}
PUT /drinks/<id>/
Updates the drink with the given ID with the given data. The request body should be a JSON object with the same fields as the POST /drinks/ endpoint.

Example request:

json
 
{
    "name": "Coke Zero",
    "price": "1.50"
}
Example response:

json
 
{
    "id": 1,
    "name": "Coke Zero",
    "price": "1.50"
}
DELETE /drinks/<id>/
Deletes the drink with the given ID.

Setup
To set up the project, follow these steps:

Install Django and Django Rest Framework:
 
pip install django djangorestframework
Create a new Django project:
 
django-admin startproject drink_api
Create a new Django app:
 
python manage.py startapp drinks
Add the drinks app to the INSTALLED_APPS list in drink_api/settings.py.
Add the following to drink_api/urls.py:
python
 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', include('drinks.urls')),
]
Create the Drink model in drinks/models.py:
python
 
from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
Create the DrinkSerializer in drinks/serializers.py:
python
 
from rest_framework import serializers
from.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'price']
Create the DrinkList and DrinkDetail views in drinks/views.py:
python
 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import DrinkSerializer
from.models import Drink
from rest_framework import status

@api_view(['GET',"POST"])
def DrinkList(request):
    #1.get objects from models
    #2.serialize the objects
    #3.return the serialised object as JsON
    if request.method == "GET":
        drinks=Drink.objects.all
        serializer=DrinkSerializer(drinks,many=True)
        return JsonResponse(serializer.data)

    if request.method == "POST":
        serializer=DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def DrinkDetail(request,id):

    try:
        drinks=Drink.objects.get(id=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer=DrinkSerializer(drinks)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=DrinkSerializer(drinks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
Create the drinks/urls.py file:
python
 
from django.urls import path
from .views import DrinkList, DrinkDetail

urlpatterns = [
    path('', DrinkList.as_view(), name='drink-list'),
    path('<int:id>/', DrinkDetail.as_view(), name='drink-detail'),
]
Run the migrations:
 
python manage.py makemigrations
python manage.py migrate
Start the development server:

python manage.py runserver
The API should now be available at http://localhost:8000/drinks/.