from django.db import models
from .baseModel import BaseModel
from .company import Company

class Room(BaseModel):

    name = models.CharField(verbose_name="Room name", max_length=100, null=False, blank=False)
    capacity = models.SmallIntegerField(verbose_name="Max capacity for the room")
    company = models.ForeignKey(Company, related_name='rooms', on_delete=models.PROTECT)

    
    def __str__(self) -> str:
        return f"{self.id} - {self.name} - {self.company.name}"

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
