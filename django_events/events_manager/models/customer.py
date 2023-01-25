from django.db import models
from .baseModel import BaseModel

class Customer(BaseModel):
    first_name = models.CharField(verbose_name="Customer first name", max_length=100, null=False, blank=False)
    last_name = models.CharField(verbose_name="Customer last name", max_length=100, null=False, blank=False)
    email = models.EmailField(verbose_name="Customer email", max_length=254, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name} - {self.email}"
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
