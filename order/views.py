from django.shortcuts import render
from order.serializers import CreateOrderSerializer, OrderSerializer, OrderItemsSerializer
from order.models import Order, OrederItems

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import (
    APIView
)
from rest_framework.generics import (
    ListAPIView
)
# Create your views here.
class OrderCreateAPIView(APIView):
    
    def post(self, request): 
        
        # request.data["added_by"] = self.request.user.id
        request.data["added_by"] = 1
        
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
        
            # return JsonResponse({
            #     "IsReport":"Success",
            #     "Msg": "Order created successfully !",
            #     # "order_id": ser
                
            # })
            return Response({
                "IsReport":"Success",
                "Msg": "Order created successfully !",
                # "data": serializer.data
                
            })  
            
class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    

    def get_queryset(self):        
        queryset =  Order.objects.all() 
        return queryset