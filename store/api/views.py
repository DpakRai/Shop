
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product
from store.api.serializers import CategorySerializer,CustomerSerializer,OrderSerializer,ProductSerializer

#Category Model
class Categorylist(APIView):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        print(category[0])
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Category Created Successfully'
        })

class Categorydetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Category to update
        category = Category.objects.get(pk=pk)

        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Category Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)

        #delete the Category
        category.delete()
        return Response({
            'message': 'Category Deleted Successfully'
        })


#Customer Model
class Customerlist(APIView):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.all()
        print(customer[0])
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Customer Created Successfully'
        })

class Customerdetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Customer to update
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Customer Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        customer = Customer.objects.get(pk=pk)

        #delete the Customer
        customer.delete()
        return Response({
            'message': 'Customer Deleted Successfully'
        })


#Order Model
class Orderlist(APIView):
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        print(order[0])
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Order Created Successfully'
        })

class Orderdetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Customer to update
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Order Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        order = Order.objects.get(pk=pk)

        #delete the Customer
        order.delete()
        return Response({
            'message': 'Order Deleted Successfully'
        })


#Product Model
class Productlist(APIView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        print(product[0])
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Product Created Successfully'
        })

class Productdetail(APIView):
    def put(self, request, pk, *args, **kwargs):
        # Get the Customer to update
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
            'message':'Product Updated Successfully'
        })

    def delete(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)

        #delete the Customer
        product.delete()
        return Response({
            'message': 'Product Deleted Successfully'
        })

        