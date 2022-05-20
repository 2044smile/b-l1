from rest_framework import serializers

from ..models import Vietnam


class VietnamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vietnam
        fields = ['id', 'area', 'description', 'temperature']
