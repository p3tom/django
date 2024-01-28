from django.contrib import admin


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

# Register your models here.
admin.site.register(AqsModel)
admin.site.register(AqsSystem)
admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(MeasurementPoint)
admin.site.register(MeasurementPointEvent)
admin.site.register(MeasurementPointHistory)
admin.site.register(MeasurementPointSensor)
admin.site.register(MeasurementPointType)
admin.site.register(Measurement)
admin.site.register(OEMManufacturer)
admin.site.register(Plant)
admin.site.register(Sensor)
admin.site.register(SensorHistory)
admin.site.register(SensorType)
admin.site.register(SensorVerification)
admin.site.register(Site)
admin.site.register(SiteContact)
admin.site.register(TagName)
admin.site.register(TagType)
admin.site.register(AQUnit)
admin.site.register(AQUnitType)
admin.site.register(MqttTopic)
admin.site.register(LoggerConfig)
admin.site.register(VersionInfo)
admin.site.register(LoggerInstance)


