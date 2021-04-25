from rest_framework import serializers
from .models import CategoryDamage

class CategoryDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDamage
        fields = ('id','name','color')