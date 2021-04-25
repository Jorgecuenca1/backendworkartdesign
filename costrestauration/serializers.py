from rest_framework import serializers
from .models import CostRestauration

class CostRestaurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostRestauration
        fields = ('id','level_damage','category_damage','type_painting','cost')