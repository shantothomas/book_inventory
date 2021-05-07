

from django.conf.urls import url
from rest_framework import routers

# from applications.api.views import superadmin
from applications.api.views import book
# from applications.api.views.admin import ViewAttendanceViewSet

book_router = routers.DefaultRouter()
book_router.register(r'Employee', book.Registration, basename="Employee")