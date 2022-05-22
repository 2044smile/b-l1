from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Vietnam
from ..serializers import VietnamSerializer
from mysite.exceptions import Error400, Error404, Error500
import logging as log


class Test400APIView(APIView):

    def get(self, request):
        try:
            t = Vietnam.objects.get(id='400')  # 400
        except ObjectDoesNotExist:
            raise Error400
        serializer = VietnamSerializer(t, many=False)
        return Response(serializer.data)


class Test404APIView(APIView):

    def get(self, request):
        try:
            t = Vietnam.objects.get(id='404')
        except ObjectDoesNotExist:
            raise Error404
        serializer = VietnamSerializer(t, many=False)
        return Response(serializer.data)


class Test500APIView(APIView):

    def get(self, request):
        try:
            t = Vietnam.objects.get(id='500')
        except ObjectDoesNotExist:
            raise Error500
        serializer = VietnamSerializer(t, many=False)
        return Response(serializer.data)