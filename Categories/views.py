from rest_framework import generics
from Categories.serializers import CategoriesSerializers,SubCategoriesSerializers
from Categories.models import Categories,Sub_Categories
from rest_framework import permissions

# Create your views here.

#Category part
class CategoriesViewSet(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers

class CategoriesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class =CategoriesSerializers

#Sub Category part
class SubCategoriesViewSet(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sub_Categories.objects.all()
    serializer_class = SubCategoriesSerializers

class SubCategoriesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sub_Categories.objects.all()
    serializer_class =SubCategoriesSerializers





