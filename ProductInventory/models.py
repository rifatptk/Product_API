from django.db import models
from Categories.models import Categories, Sub_Categories

# Create your models here.


class Image(models.Model):
    property_id = models.ForeignKey(
                    'properties.Address',
                    null=False,
                    default=1,
                    on_delete=models.CASCADE
                )
    image = models.ImageField(upload_to='media')


class Products(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.CharField(max_length=250, null=False, blank=False)
    meta = models.TextField(max_length=500, null=True, blank=True)
    descriptions = models.TextField(max_length=500, null=True, blank=True)
    alter_text = models.CharField(max_length=100, null=True, blank=True)
    is_active= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    feature_image=models.ImageField(upload_to='media')

    category = models.ManyToManyField(Categories)
    sub_category = models.ManyToManyField(Sub_Categories)
    #problem is here 
    property = models.ForeignKey(Image, default=None, on_delete=models.CASCADE,)

    def __str__(self) -> str:
        return self.name






    
