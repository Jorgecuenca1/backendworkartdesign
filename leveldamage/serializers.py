from rest_framework import serializers
from .models import LevelDamage

class LevelDamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelDamage
        fields = ('id','name')