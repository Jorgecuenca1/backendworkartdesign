from rest_framework import serializers
from .models import TypePainting

class TypePaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePainting
        fields = ('id','name')