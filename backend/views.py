from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, RoomSerializer, MenuEntrySerializer
from .models import User, Room, MenuEntry
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


@method_decorator(csrf_exempt, name='dispatch')
class EnterRoom(APIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        print(request.data[0])

        queryset = Room.objects.all().filter(id=request.data[0]["rid"])

        room = queryset.first()

        print(room)

        return Response(status=204)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuEntryViewSet(viewsets.ModelViewSet):
    queryset = MenuEntry.objects.all()
    serializer_class = MenuEntrySerializer
