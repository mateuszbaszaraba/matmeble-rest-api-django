from .serializers import ProductSerializer, SoftFurnsSerializer, ArmchairSerializer
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import SoftFurniture, Armchair, Product

furn_types = ('kanapa', 'narożnik', 'wersalka', 'łóżko')


class ProductsView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format=None):
        soft_furns = SoftFurniture.objects.all()
        armchairs = Armchair.objects.all()
        soft_furns_serialized = SoftFurnsSerializer(soft_furns, many=True)
        armchairs_serialized = ArmchairSerializer(armchairs, many=True)
        result_model = soft_furns_serialized.data + armchairs_serialized.data
        return Response(result_model)

    def post(self, request, format=None):
        furn_type = request.data['type']

        if furn_type in furn_types:
            serializer = SoftFurnsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ArmchairSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('pk')

        if SoftFurniture.objects.filter(slug=slug):
            serialized_data = SoftFurnsSerializer(SoftFurniture.objects.get(slug=slug))
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        elif Armchair.objects.filter(slug=slug):
            serialized_data = ArmchairSerializer(Armchair.objects.get(slug=slug))
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
