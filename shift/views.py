from .models import User, Shift, WorkerShift
from .serializers import ShiftSerializer, ShiftCreateSerializer, WorkerShiftSerializer


from rest_framework.response import Response
from rest_framework import permissions, status, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError

# own created persimission classes
from common.permissions import IsSuperUser 
from common.paginations import CustomPagination 

from common.enums import StatusTypes
from rest_framework.generics import (
    ListCreateAPIView,
    )


# Shifts create, list

class ShiftListCreateAPIView(ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = (IsSuperUser,)  # only superuser can create a shift
    pagination_class = CustomPagination    
    
    
    def create(self, request):
        request.data["added_by"] = self.request.user.id
        
        serializer = ShiftCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )

# Assign shifts to workers
class WorkerShiftListCreateAPIView(ListCreateAPIView):
    
    queryset = WorkerShift.objects.all()
    serializer_class = WorkerShiftSerializer
    permission_classes = (IsSuperUser,)
    
    def create(self, request, *args, **kwargs):
        try:
            
            shift = Shift.objects.get(pk=request.data['shift_id'], status=StatusTypes.ACTIVE.value)
            print(shift)
            return Response({
                "msg": "testing"
            })
        except Shift.DoesNotExist:
            raise ValidationError(detail='invalid shift_id provided', code=status.HTTP_404_NOT_FOUND)
        
