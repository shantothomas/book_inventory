from rest_framework import routers

# from applications.api.views import superadmin
from applications.api.views import book
# from applications.api.views.admin import ViewAttendanceViewSet
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken

book_router = routers.DefaultRouter()
book_router.register(r'EmployeeRegistration', book.Registration, basename="Employee")
book_router.register(r'EmployeeLogin', book.EmployeeLogin, basename="EmployeeLogin")
book_router.register(r'AddingBook', book.AddingBook, basename="EmployeeLogin")
book_router.register(r'Borrow', book.Borrow, basename="Borrow")
# book_router.register(r'AddingBook', book.AddingBook, basename="EmployeeLogin")