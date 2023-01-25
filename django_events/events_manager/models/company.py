from django.db import models
from .baseModel import BaseModel

class Company(BaseModel):
    name = models.CharField(verbose_name="Company name", max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
