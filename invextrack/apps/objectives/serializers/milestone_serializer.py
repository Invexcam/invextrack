from rest_framework import serializers
from ..models.milestone import Milestone

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'