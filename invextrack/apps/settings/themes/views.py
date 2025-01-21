from rest_framework import viewsets
from .models import Theme
from .serializers import ThemeSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer