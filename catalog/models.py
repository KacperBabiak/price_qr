from django.db import models
from django.urls import reverse

class Product(models.Model):
    # Fields
    name = models.CharField(max_length=50, help_text='Products name')
    price = models.FloatField(max_length=4, help_text='Products price')

    # Metadata
    class Meta:
        ordering = ['name','price']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Product."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the Product object (in Admin site etc.)."""
        return self.name
