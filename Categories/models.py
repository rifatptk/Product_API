from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name=models.CharField(max_length=100, null=False, blank=False)
    slug=models.CharField(max_length=255, null=False, blank=False)
    image=models.ImageField(upload_to='media', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_code=models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name
# Create your models here.
class Sub_Categories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_category_name=models.CharField(max_length=100, null=False, blank=False)
    slug=models.CharField(max_length=255, null=False, blank=False)
    image=models.ImageField(upload_to='media', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description=models.TextField(max_length=1500, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.sub_category_name





