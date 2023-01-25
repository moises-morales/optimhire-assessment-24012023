from django.db import models


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(active=False)


class BaseModel(models.Model):
    created = models.DateField(verbose_name="Date when the object was added", auto_now_add=True, editable=False)
    modified = models.DateField(verbose_name="Data for the last edition", auto_now=True, editable=False)
    active = models.BooleanField(verbose_name="Is active the record?(logical deletion)", default= True)

    objects = BaseModelManager()

    def delete(self):
        if self.active:
            self.active = False
        self.save()

    class Meta:
        abstract = True
