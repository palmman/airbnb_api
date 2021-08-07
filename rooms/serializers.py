from django.http import request
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import HostRooms




class HomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HostRooms
        fields = '__all__'


class CreateRoomSerializer(serializers.ModelSerializer):

    booking = serializers.BooleanField(default=True)

    class Meta:
        model = HostRooms
        fields = '__all__'


    
    # def create(self, validated_data):

    #     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
        
    #     room = HostRooms.objects.create(
    #         name=validated_data['name'],
    #         address=validated_data['address'],
    #         description=validated_data['description'],
    #         room_image=validated_data['room_image'],
    #         price=validated_data['price']
    #     )
    #     room.save()

    #     return room