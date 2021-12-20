from rest_framework import serializers
from .models import *


class OfferSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id','title','price','category_id',)


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'