from django.contrib import admin
from django.urls import path, include
from BlogCorea.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogcorea/', include('BlogCorea.urls')),
]
