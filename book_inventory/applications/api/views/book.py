# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, status

from applications.api.serializers import book
from bookapp.models import Books


class Registration(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = book.RegitrationSerializer

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=False):
                return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)

            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response({'promptmsg': 'Sucessfully added', 'data': serializer.data},
                            status=status.HTTP_201_CREATED,
                            headers=headers)

class EmployeeLogin(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = book.EmlployeeLoginSerializer

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid(raise_exception=False):
                return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)

            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)
            return Response({'promptmsg': 'Sucessfully Login', 'data': serializer.data},
                            status=status.HTTP_201_CREATED,
                            headers=headers)
class AddingBook(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = book.AddingBookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)

class Borrow(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = book.AddingBookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    # def update(self, request, *args, **kwargs):
    #     try:
    #         # print("hiii")
    #         instance = self.get_object()
    #         instance.bookname = request.data.get("bookname")
    #         instance.quantity = request.data.get("quantity")
    #         instance.quantity = request.data.get("quantity")
    #         # print(instance)
    #         instance.save()
    #         serializer = self.get_serializer(instance)
    #         return Response({'promptmsg': 'Successfully Updated', 'data': serializer.data},
    #                         status=status.HTTP_201_CREATED,
    #                         )
    #     except:
    #         return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)