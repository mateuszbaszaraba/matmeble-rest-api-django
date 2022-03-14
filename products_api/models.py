from django.db import models
import uuid
from django.template.defaultfilters import slugify


def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)


class Product(models.Model):
    headrest_options = (
        ('regulowany', 'Regulowany'),
        ('nieregulowany', 'Nieregulowany'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to)

    height = models.CharField(max_length=30)
    width = models.CharField(max_length=30)
    depth = models.CharField(max_length=30)

    seat_depth = models.CharField(max_length=30)
    container = models.IntegerField(null=True, blank=True)
    headrest = models.CharField(null=True, blank=True, choices=headrest_options, default='nieregulowany',
                                max_length=30)

    def slug(self):
        return slugify(self.title)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class SoftFurniture(Product):
    arm_options = (
        ('tapicerowane', 'Tapicerowane'),
        ('drewniane', 'Drewniane'),
    )

    arm = models.CharField(max_length=50, null=True, blank=True, choices=arm_options,
                           default='tapicerowane')
    sleep_func = models.BooleanField(null=True, blank=True, default=True)
    sleep_dim = models.CharField(max_length=30, null=True, blank=True)


class Armchair(Product):
    trim_options = (
        ('niklowane', 'Niklowane'),
        ('drewniane', 'Drewniane'),
    )

    trim = models.CharField(max_length=50, null=True, blank=True, choices=trim_options,
                           default='drewniane')
