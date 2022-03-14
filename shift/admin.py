from django.contrib import admin
from .models import Shift, WorkerShift
# Register your models here.
admin.site.register(Shift)
admin.site.register(WorkerShift)