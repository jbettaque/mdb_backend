from rest_framework import serializers
from .models import Room, User, MenuEntry


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MenuEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuEntry
        fields = "__all__"

