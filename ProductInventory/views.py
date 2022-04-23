import imp
from django.shortcuts import render
from ProductInventory.models import Products,Image
from rest_framework import generics
from rest_framework import permissions
from ProductInventory.serializers import ProductSerializers, ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http.multipartparser import MultiPartParser

from django.http import JsonResponse

# Create your views here.

class ProductView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializers




#  problem is here 
class ImageView(APIView):
    parser_classes = (MultiPartParser)

    def get(self, request):
        all_images = Image.objects.all()
        serializer = ImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        property_id = request.data['property_id']

        # converts querydict to original dict
        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(property_id,
                                                            img_name)
            file_serializer = ImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)