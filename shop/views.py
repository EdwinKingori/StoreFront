from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


@api_view()
def product_list(request):
    return Response('Ok')


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    # converts the product object to a dictionary
    serializer = ProductSerializer(product)
    return Response(serializer.data)
