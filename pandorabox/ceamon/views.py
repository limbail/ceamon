from django.shortcuts import render
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
# IMPORT REST
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from ceamon.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User, Group
from ceamon.serializers import UserSerializer, GroupSerializer

# IMPORT 
from ceamon.serializers import sapnodeSerializer, StatusSerializer
from ceamon.models import sapnode, StatusModel


def detail(request, question_id):
    return HttpResponse("Estas viendo el server %s." % server_id)

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def sapnode_list(request, format=None):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }

    if request.method == 'GET':
        l_sapnode = sapnode.objects.all()
        serializer = sapnodeSerializer(l_sapnode, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = sapnodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def sapnode_detail(request, pk, format=None):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    try:
        l_sapnode = sapnode.objects.get(pk=pk)
    except sapnode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = sapnodeSerializer(l_sapnode)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = sapnodeSerializer(l_sapnode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = sapnodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        l_sapnode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET', 'PUT' , 'POST'])
def StatusViewSet(request, format=None):
    #l_StatusModel = StatusModel.objects.all(pk=pk)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }

    if request.method == 'GET':
        l_StatusModel = StatusModel.objects.all()
        serializer = StatusSerializer(l_StatusModel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def status_detail(request, pk, format=None):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    try:
        l_StatusModel = StatusModel.objects.get(pk=pk)
    except StatusModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatusSerializer(l_StatusModel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StatusSerializer(l_StatusModel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        StatusModel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

