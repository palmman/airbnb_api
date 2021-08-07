

from rest_framework import generics
from rest_framework import serializers, permissions
from .serializers import CreateRoomSerializer, HomeSerializer


from .models import HostRooms

# Create your views here.

class HomeAPIView(generics.ListAPIView):

    queryset = HostRooms.objects.all()
    serializer_class = HomeSerializer

class RoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = HostRooms.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateRoomAPI(generics.ListCreateAPIView):

    queryset = HostRooms.objects.all()
    serializer_class = CreateRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner = self.request.user.account)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UpdateRoomAPI(generics.UpdateAPIView):

    queryset = HostRooms.objects.all()
    serializer_class = CreateRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


    def update(self, request, *args, **kwargs):
    # some logic

        instance = self.get_object()
        return super().update(request, *args, **kwargs)

    
