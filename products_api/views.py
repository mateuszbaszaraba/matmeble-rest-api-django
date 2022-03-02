from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class Products(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()

    def list(self, request):
        serializer_class = ProductSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, slug=pk)
        serializer_class = ProductSerializer(post)
        return Response(serializer_class.data)
