from typing import Dict
from rest_framework import serializers
from .models import User, Order, OrederItems


class OrderSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):   
    class Meta:
        model = OrederItems
        fields = '__all__'

class CreateOrderSerializer(serializers.ModelSerializer):  
    order_items = OrderItemsSerializer(many=True)
    

    class Meta:
        model = Order
        fields = '__all__'
        extra_fields = ['order_items']
    
    def create(self, validated_data):
        popped_order_items = validated_data.pop('order_items')
        

        order = Order.objects.create(**validated_data)        

        
        

        for i in popped_order_items:
            si = OrederItems.objects.create(order = order, **i)
            print(si.pk)        
        
        print(order.id)
        
        return order

        
