from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Vietnam


class VietnamSerializer(serializers.ModelSerializer):
    area = serializers.CharField(max_length=30)

    def validate(self, data):
        if data['area'] not in ['하노이', '하롱베이', '다낭', '나트랑']:
            raise ValidationError("한글로 된 베트남 여행지가 들어가야 합니다.")
        return data

    class Meta:
        model = Vietnam
        fields = ['id', 'area', 'description', 'temperature']
