from django.urls import path
from .views import sensor_list

urlpatterns = [
    path('sensor_list/', sensor_list, name='sensor_list'),
    #path('sensor_detail/<int:sensor_id>/', sensor_detail, name='sensor_detail'),
    # Add other paths as needed
]
