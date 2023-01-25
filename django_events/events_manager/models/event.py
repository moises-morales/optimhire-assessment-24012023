from django.db import models
from .baseModel import BaseModel
from .company import Company
from .room import Room

class Event(BaseModel):

    name = models.CharField(verbose_name="Event name", max_length=100, null=False, blank=False)
    date = models.DateField(verbose_name="Event date")
    public = models.BooleanField(verbose_name="Is a public event?", default=True)
    room = models.ForeignKey(Room, related_name='events', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, related_name='events', on_delete=models.PROTECT)

    
    def __str__(self) -> str:
        return f"{self.name} - {self.company.name}"

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
