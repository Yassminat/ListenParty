from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    # Outgoing serializer to serialize response Room 
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')

class CreateRoomSerializer(serializers.ModelSerializer): 
    #Serializer for post requests for creating a room 
    class Meta: 
        model = Room #Model that this serializer will serialize into 
        fields = ('guest_can_pause', 'votes_to_skip') #Fields we want from the post request
