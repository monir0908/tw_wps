from django.urls import path
from .views import (
    OrderCreateAPIView,
    OrderListAPIView
    
    )

urlpatterns = [
    path('create-order', OrderCreateAPIView.as_view(), name='create-order'),
    path('', OrderListAPIView.as_view(), name='order-list'),
]