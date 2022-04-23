from rest_framework import serializers
from ProductInventory.models import Products, Image


class ProductSerializers(serializers.ModelSerializer):

    feature_image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)

    class Meta:
        model=Products
        fields = ['category','sub_category', 'name', 'slug','meta', 'descriptions', 'alter_text', 'is_active', 'feature_image']




#problem is here
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'property_id',
            'image'
        )

