from this import d
from django.shortcuts import render
from .models import User, Shift, WorkerShift
from .serializers import ShiftSerializer, WorkerShiftSerializer

from rest_framework.generics import (
    ListCreateAPIView,
    )


# Creating shifts

class ShiftListCreateAPIView(ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

class WorkerShiftListCreateAPIView(ListCreateAPIView):
    
    queryset = WorkerShift.objects.all()
    serializer_class = WorkerShiftSerializer
        
