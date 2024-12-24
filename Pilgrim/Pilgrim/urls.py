


from django.contrib import admin
from django.urls import path, re_path
from app.views import *

from app.views import viewer

urlpatterns = [
    path('admin/', admin.site.urls),
 path('1/', viewer, name='viewer'),
 path('', viewhtml, name='viewhtml'),
]




