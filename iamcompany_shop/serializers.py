from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 50)
    product_photo = serializers.ImageField() 
    cost = serializers.IntegerField()
    category = serializers.CharField(max_length = 50)
    slug = serializers.SlugField() 
    size = serializers.IntegerField()
    weight = serializers.CharField(max_length = 50) 