from rest_framework import serializers
from .models import Waterfall

class WaterfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waterfall
        fields = '__all__'
