from rest_framework import serializers
from . models import blogpost

class blogpostSerializers(serializers.ModelSerializer):
    class Meta:
        model = blogpost
        fields = ['name', 'blog', 'date']