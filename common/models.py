import uuid
from django.db import models

from django.db.models import CharField, Model
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField


from .enums import StatusTypes
from .fields import TimestampImageField


class BaseModel(models.Model):
    alias = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        unique=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NameBaseModel(BaseModel):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    slug = AutoSlugField(
        populate_from='first_name',
        always_update=True,
        unique=True,
        allow_unicode=True
    )

    class Meta:
        abstract = True



    
