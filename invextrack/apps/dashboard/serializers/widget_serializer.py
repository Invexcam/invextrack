from rest_framework import serializers
from ..models.widget import Widget

class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = '__all__'