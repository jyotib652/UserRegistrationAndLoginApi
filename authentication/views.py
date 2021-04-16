from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class MessageView(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        content = {'message': 'Successfully obtained JWT token'}
        return Response(content)


