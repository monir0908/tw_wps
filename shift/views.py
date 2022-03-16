from .models import User, Shift, WorkerShift
from .serializers import ShiftSerializer, WorkerShiftSerializer


from rest_framework.response import Response
from rest_framework import permissions, status, filters


from rest_framework.generics import (
    ListCreateAPIView,
    )


# Creating shifts

class ShiftListCreateAPIView(ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    
    
    def post(self, request):
        print(request.data)
        serializer = ShiftSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )

class WorkerShiftListCreateAPIView(ListCreateAPIView):
    
    queryset = WorkerShift.objects.all()
    serializer_class = WorkerShiftSerializer
        
