from typing import Dict
from rest_framework import serializers
from .models import User, Shift, WorkerShift
from core.serializers import UserSerializer, WorkerSerializer

class ShiftSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField()
    class Meta:
        model = Shift
        fields = '__all__'
        extra_fields = ['added_by']

class WorkerShiftSerializer(serializers.ModelSerializer):
    worker_detail = serializers.SerializerMethodField()
    shift_detail = serializers.SerializerMethodField()
    class Meta:
        model = WorkerShift
        fields = [
            'id',
            'alias',
            'created_at',
            'updated_at',
            'worker_detail',
            'shift_detail'
        ]
        
    def get_worker_detail(self, instance:WorkerShift)-> User:
            return WorkerSerializer(instance.worker).data 
              
    def get_shift_detail(self, instance:WorkerShift)-> Shift:
            return ShiftSerializer(instance.shift).data