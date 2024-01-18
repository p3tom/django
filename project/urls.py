# project/urls.py
# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myapp/', include('myapp.urls')),
# ]
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # other paths
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
