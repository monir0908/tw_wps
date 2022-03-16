from django.urls import path
from .views import (
    ShiftListCreateAPIView,
    WorkerShiftListCreateAPIView,
    )

urlpatterns = [
    path('', ShiftListCreateAPIView.as_view(), name='shift'),
    path('worker-shift', WorkerShiftListCreateAPIView.as_view(), name='worker-shift'),
]