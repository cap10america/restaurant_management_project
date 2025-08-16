from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Item , Restaurant
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.

def homepage(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.name if restaurant else "Our Restaurant"
    phone_number = getattr(settings,'RESTAURANT_PHONE',"Not availabe")
    return render(request ,'homepage.html' ,{'restaurant_name':restaurant_name,'phone_number':phone_number})
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuView(APIView):
    def get(self,request):
        menus =Menu.objects.all()
        serializer=MenuSerializer(menus,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MenuAPIView(APIView):
    def get(self,request):
        menu =[
            
            {"name":"pizza a","description":"pizza made with a","price" :299 }
            {"name":"burger" ,"description" :"burgeer with chicken","price":200}
        ]
        return Response(menu,status =stauts.HTTP_200_OK+)