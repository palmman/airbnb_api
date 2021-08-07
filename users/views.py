from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics
from .serializers import AccountSerializer, RegisterSerializer, MyTokenObtainPairSerializer, UpdateAccountSerializer



from .models import Account


class AccountAPIView(generics.RetrieveAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return Account.objects.filter(room=id_)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UpdateAccountView(generics.UpdateAPIView):

    queryset = Account.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateAccountSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokenObtainPairSerializer