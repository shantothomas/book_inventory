from django.shortcuts import render

# Create your views here.
# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, status

# from applications.api.serializers import book
from bookapp.serializers import RegitrationSerializer


class Registration(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = RegitrationSerializer

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=False):
                return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)

            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response({'promptmsg': 'Sucessfully added', 'data': serializer.data},
                            status=status.HTTP_201_CREATED,
                            headers=headers)