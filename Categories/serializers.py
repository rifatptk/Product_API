from rest_framework import serializers
from Categories.models import Categories, Sub_Categories

class CategoriesSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = Categories
        fields = ['category_name','slug','image','category_code','is_active']

class SubCategoriesSerializers(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="Categories:categories-detail")
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True, required=False)
    class Meta:
        model = Sub_Categories
        fields = ['category' ,'sub_category_name', 'slug', 'image', 'description', 'is_active']

