from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def product_list(request, *args, **kwargs):
    # data = request.data
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer)
        serializer.save()
        # serializer.save(owner=self.request.user)



class ProductDetailAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'