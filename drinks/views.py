from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DrinkSerializer
from .models import Drink
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

