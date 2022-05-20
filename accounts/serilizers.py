from atexit import register
from rest_framework import serializers
from .models import introduction

class introductionserializer(serializers.ModelSerializer):

    class Meta:
        model = register
        fields = ['username', 'email', 'password']