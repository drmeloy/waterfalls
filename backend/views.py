from backend.models import Waterfall
from rest_framework import viewsets
from .serializers import WaterfallSerializer

# Waterfall Viewset
class WaterfallViewSet(viewsets.ModelViewSet):
  queryset = Waterfall.objects.all()
  serializer_class = WaterfallSerializer
