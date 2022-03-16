from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import BaseModel
from .enums import ShiftStatus
from core.models import User

# Master table regarding SHIFT
class Shift(BaseModel):
    shift_title= models.CharField(max_length=250)
    shift_start = models.TimeField( blank=True, null=True)
    shift_end = models.TimeField( blank=True, null=True)
    shift_session= models.CharField(max_length=250)
    shift_short_code= models.CharField(max_length=100)
    status = models.IntegerField(
        choices=[(tag.value, _(tag.name)) for tag in ShiftStatus],
        default=ShiftStatus.ACTIVE.value
    )
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, db_column="added_by"
    )
    
    class Meta:
        db_table = 'shifts'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['shift_title']),
            models.Index(fields=['shift_session']),
            models.Index(fields=['-created_at']),
        ]   
    
    def __str__(self):
        return 'shift_session: {}'.format(self.shift_session)

# One to many relationship between worker and shift
class WorkerShift(BaseModel):
    worker = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    shift = models.ForeignKey(
        Shift, on_delete=models.CASCADE, blank=True, null=True
    )
    
    class Meta:
        db_table = 'worker_shifts'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]   
    
    def __str__(self):
        return 'primary_key: {}'.format(self.id)