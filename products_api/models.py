from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)

    height = models.CharField(max_length=30)
    width = models.CharField(max_length=30)
    depth = models.CharField(max_length=30)
    sleep_dim = models.CharField(max_length=30, null=True, blank=True)
    seat_depth = models.CharField(max_length=30)

    sleep_func = models.BooleanField(null=True, blank=True)
    container = models.IntegerField(null=True, blank=True)
    arm = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
