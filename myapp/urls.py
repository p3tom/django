from django.urls import path
from . import views


urlpatterns = [

        # Add other paths as needed
    
    path('home/', views.home, name='home'),
    path('aqsmodel/', views.aqsmodel, name='aqsmodel'),
    path('aqssystem/', views.aqssystem, name='aqssystem'),
    path('customer/', views.customer, name='customer'),
    path('event/', views.event, name='event'),
    path('measurement_pt/', views.measurement_pt, name='measurement_pt'),
    path('measurement_pt_event/', views.measurement_pt_event, name='measurement_pt_event'),
    path('measurement_pt_history/', views.measurement_pt_history, name='measurement_pt_history'),
    path('measurement_pt_sensor/', views.measurement_pt_sensor, name='measurement_pt_sensor'),
    path('measurement_pt_type/', views.measurement_pt_type, name='measurement_pt_type'),
    path('measurement/', views.measurement, name='measurement'),
    path('oem_manufacturer/', views.oem_manufacturer, name='oem_manufacturer'),
    path('plant/', views.plant, name='plant'),
    path('sensor/', views.sensor, name='sensor'),
    path('sensor_history/', views.sensor_history, name='sensor_history'),
    path('sensor_type/', views.sensor_type, name='sensor_type'),
    path('sensor_verification/', views.sensor_verification, name='sensor_verification'),
    path('site/', views.site, name='site'),
    path('site_contact/', views.site_contact, name='site_contact'),
    path('tag_name/', views.tag_name, name='tag_name'),  
    path('aq_unit/', views.aq_unit, name='aq_unit'),  
    path('aq_unit_type/', views.aq_unit_type, name='aq_unit_type'), 
    path('mqtt_topic/', views.mqtt_topic, name='mqtt_topic'), 
    path('logger_config/', views.logger_config, name='logger_config'),
    path('version_info/', views.version_info, name='version_info'), 
    path('tag_type/', views.tag_type, name='tag_type'),  
    path('logger_instance/', views.logger_instance, name='logger_instance'),     


]
