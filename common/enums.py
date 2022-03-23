from enum import Enum


class StatusTypes(Enum):  
    ACTIVE = 1
    INACTIVE = 2
    
class OrderStatus(Enum):  
    PENDING = 1
    DELIVERED = 2