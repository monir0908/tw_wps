from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import BaseModel
from common.enums import OrderStatus
from core.models import User

# Master table regarding SHIFT
class Order(BaseModel):
    order_total_amount= models.IntegerField(default=0)
    status = models.IntegerField(
        choices=[(tag.value, _(tag.name)) for tag in OrderStatus],
        default=OrderStatus.PENDING.value
    )
    
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="customer"
    )
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, db_column="added_by"
    )
    
    class Meta:
        db_table = 'orders'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]   
    
    def __str__(self):
        return 'order_pk: {}'.format(self.pk)

# One to many relationship between order and order-items
class OrederItems(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True, related_name="order"
    )
    item_name = models.CharField(max_length=250, blank=False)
    item_price = models.BigIntegerField(default=0)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, db_column="added_by"
    )
    class Meta:
        db_table = 'order_items'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]   
    
    def __str__(self):
        return 'primary_key: {}'.format(self.id)