import logging
logger = logging.getLogger(__name__)
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import Avg, Count, Min, Sum
from django.db.models.signals import post_delete
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel, NameBaseModel

from .enums import GenderTypes
from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin, NameBaseModel):       
    
    # email will be considered as username, password will automatically be mandatory
    email = models.EmailField(db_index=True, unique=True, max_length=200)
    mobile = models.CharField(max_length=30, blank=True, null=True, default=None)
    
    address_one = models.TextField(max_length=500,  blank=True, null=True, default=None)
    address_two = models.TextField(max_length=500,  blank=True, null=True, default=None)
    dob = models.DateField( blank=True, null=True)
    gender = models.IntegerField(
        choices=[(tag.value, _(tag.name)) for tag in GenderTypes],
        default=GenderTypes.NONE.value
    )
    
    
    is_worker = models.BooleanField( blank=True, null=True, default=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Whether this user should be treated as active. Unselect\
             this instead of deleting accounts.')) 
    is_superuser = models.BooleanField( blank=True, null=True, default=False)
    
    # explicit fields    
    # last_login
    # date_joined
    #first_name, last_name, slug coming from NameBaseModel
    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name','last_name','mobile',)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    

    def __unicode__(self):
        return u"username: {}".format(self.email)
    
    def get_full_name(self):
        """ Returns the full name """
        name = u"{}".format(self.first_name + " " + self.last_name)
        return name.strip()

    def get_short_name(self):
        return u"{}".format(self.first_name)

    def __str__(self):
        return self.get_full_name()

    