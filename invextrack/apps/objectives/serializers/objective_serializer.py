from rest_framework import serializers
from ..models.objective import Objective

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'