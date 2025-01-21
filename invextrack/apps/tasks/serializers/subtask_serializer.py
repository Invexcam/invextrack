from rest_framework import serializers
from ..models.subtask import Subtask

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'