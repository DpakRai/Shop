from rest_framework import serializers
from store.models.category  import Category
from store.models.customer  import Customer
from store.models.orders  import Order
from store.models.product  import Product


#Category Model Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)

#Customer Model Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

#Orders Model Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

#Product Model Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'