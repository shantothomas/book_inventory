
from django.conf.urls import url

from django.urls import include

from applications.api.urls.books import book_router

urlpatterns = [
    url(r'^books/', include(book_router.urls)),


]
