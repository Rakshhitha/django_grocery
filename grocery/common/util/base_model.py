from django.db import models

# Create your models here.


class BaseModelMixin(models.Model):
    deletedAt = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    ACTIVE = '1'
    DELETED = '2'
    STATUS = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )
    status = models.CharField(max_length=10, choices=STATUS, default=ACTIVE)

    class Meta:
        abstract = True
