from django.http import Http404
from crud.models import blogpost
from . models import blogpost
from . serializers import blogpostSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class blogpostGetPostView(APIView):
    def get(self, request):
        courses = blogpost.objects.all()
        serializer = blogpostSerializers(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = blogpostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class blogpostView(APIView):

    def get_profile(self, pk):
        try:
            return blogpost.objects.get(username=pk)
        except blogpost.DoesNotExist:
            raise (Http404)

    def get(self, request, pk):
        course = self.get_profile(pk)
        serializer = blogpostSerializers(course, many=False)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = self.get_profile(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        course = self.get_profile(pk)
        serializer = blogpostSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)