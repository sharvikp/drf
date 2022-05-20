from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.views import APIView



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class UserAPIView(APIView):
    # permission_classes = (IsAuthenticated)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

