from django.views.generic import CreateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Vietnam
from ..serializers import VietnamSerializer


@api_view(['GET'])
def list_vietnam(request):
    v = Vietnam.objects.all()
    serializer = VietnamSerializer(v, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_vietnam(request, pk):
    v = Vietnam.objects.get(id=pk)
    serializer = VietnamSerializer(v, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_vietnam(request):
    serializer = VietnamSerializer(data=request.data)

    if request.method == 'GET':
        v = Vietnam.objects.all()
        serializer = VietnamSerializer(v, many=True)
        return Response(serializer.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print('invalid - 10일이라 시간이 없다, 시간이 더 많았다면 Exception을 만들었을 것')

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def put_vietnam(request, pk):
    v = Vietnam.objects.get(id=pk)
    serializer = VietnamSerializer(instance=v, data=request.data)

    if request.method == 'GET':
        serializer = VietnamSerializer(v)
        return Response(serializer.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print('invalid update - 10일이라 시간이 없다, 시간이 더 많았다면 Exception을 만들었을 것')

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def delete_vietnam(request, pk):
    v = Vietnam.objects.get(id=pk)

    if request.method == 'GET':
        serializer = VietnamSerializer(v)
        return Response(serializer.data)

    if v:
        v.delete()
    else:
        print('Not Delete - 10일이라 시간이 없다, 시간이 더 많았다면 Exception을 만들었을 것')

    return Response(f"Delete {pk}")
