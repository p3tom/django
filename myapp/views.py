# # myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

from .models import AqsModel
from .models import AqsSystem
from .models import Customer
from .models import Event
from .models import MeasurementPoint
from .models import MeasurementPointEvent
from .models import MeasurementPointHistory
from .models import MeasurementPointSensor
from .models import MeasurementPointType
from .models import Measurement
from .models import OEMManufacturer
from .models import Plant
from .models import Sensor
from .models import SensorHistory
from .models import SensorType
from .models import SensorVerification
from .models import Site
from .models import SiteContact
from .models import TagName
from .models import AQUnit
from .models import AQUnitType
from .models import MqttTopic
from .models import LoggerConfig
from .models import VersionInfo
from .models import TagType
from .models import LoggerInstance


def home(request):
    return render(request, 'home.html')
 
def aqsmodel(request):
  aqsmodels = AqsModel.objects.all()
  return render(request, 'aqsmodel.html', {'aqsmodels': aqsmodels})

def aqssystem(request):
  aqssystems = AqsSystem.objects.all()
  return render(request, 'aqssystem.html', {'aqssystems': aqssystems})

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def measurement_pt(request):
    measurement_pts = MeasurementPoint.objects.all()
    return render(request, 'measurement_pt.html', {'measurement_pts': measurement_pts})

def measurement_pt_event(request):
    measurement_pt_events = MeasurementPointEvent.objects.all()
    return render(request, 'measurement_pt_event.html', {'measurement_pt_events': measurement_pt_events})

def measurement_pt_history(request):
    measurement_pt_historys = MeasurementPointHistory.objects.all()
    return render(request, 'measurement_pt_history.html', {'measurement_pt_historys': measurement_pt_historys})

def measurement_pt_sensor(request):
    measurement_pt_sensors = MeasurementPointSensor.objects.all()
    return render(request, 'measurement_pt_sensor.html', {'measurement_pt_sensors': measurement_pt_sensors})

def measurement_pt_type(request):
    measurement_pt_types = MeasurementPointType.objects.all()
    return render(request, 'measurement_pt_type.html', {'measurement_pt_types': measurement_pt_types})

def measurement(request):
    measurements = Measurement.objects.all()
    return render(request, 'measurement.html', {'measurements': measurements})

def oem_manufacturer(request):
    oem_manufacturers = OEMManufacturer.objects.all()
    return render(request, 'oem_manufacturer.html', {'oem_manufacturers': oem_manufacturers})

def plant(request):
    plants = Plant.objects.all()
    return render(request, 'plant.html', {'plants': plants})

def sensor(request):
    sensors = Sensor.objects.all()
    return render(request, 'sensor.html', {'sensors': sensors})   

def sensor_history(request):
    sensor_historys = SensorHistory.objects.all()
    return render(request, 'sensor_history.html', {'sensor_historys': sensor_historys})  

def sensor_type(request):
    sensor_types = SensorType.objects.all()
    return render(request, 'sensor_type.html', {'sensor_types': sensor_types})

def sensor_verification(request):
    sensor_verifications = SensorVerification.objects.all()
    return render(request, 'sensor_verification.html', {'sensor_verifications': sensor_verifications})  

def site(request):
    sites = Site.objects.all()
    return render(request, 'site.html', {'sites': sites})

def site_contact(request):
    site_contacts = SiteContact.objects.all()
    return render(request, 'site_contact.html', {'site_contacts': site_contacts})    

def tag_name(request):
    tag_names = TagName.objects.all()
    return render(request, 'tag_name.html', {'tag_names': tag_names})   

def aq_unit(request):
    aq_units = AQUnit.objects.all()
    return render(request, 'aq_unit.html', {'aq_units': aq_units})

def aq_unit_type(request):
    aq_unit_types = AQUnitType.objects.all()
    return render(request, 'aq_unit_type.html', {'aq_unit_types': aq_unit_types}) 

def mqtt_topic(request):
    mqtt_topics = MqttTopic.objects.all()
    return render(request, 'mqtt_topic.html', {'mqtt_topics': mqtt_topics})

def logger_config(request): 
    logger_configs = LoggerConfig.objects.all() 
    return render(request, 'logger_config.html', {'logger_configs': logger_configs})

def version_info(request):
    version_infos = VersionInfo.objects.all()
    return render(request, 'version_info.html', {'version_infos': version_infos})  

def tag_type(request):
    tag_types = TagType.objects.all()
    return render(request, 'tag_type.html', {'tag_types': tag_types})  

def logger_instance(request):
    logger_instances = LoggerInstance.objects.all()
    return render(request, 'logger_instance.html', {'logger_instances': logger_instances})   