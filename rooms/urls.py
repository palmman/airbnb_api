from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeAPIView.as_view(), name='home' ),
    path('room/<int:pk>', views.RoomDetailAPIView.as_view(), name='room_detail'),

    path('room/create_room/', views.CreateRoomAPI.as_view(), name='room_detail'),
    path('room/edit_room/<int:pk>', views.UpdateRoomAPI.as_view(), name='edit_room'),

    
]
