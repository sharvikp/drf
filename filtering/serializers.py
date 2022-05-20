from rest_framework import serializers
from .models import introduction

class introductionserializer(serializers.ModelSerializer):

    class Meta:
        model = introduction
        fields = ['id', 'name', 'intro', 'video_link']