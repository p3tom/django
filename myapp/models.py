  #myapp/models.py

from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.apps import apps


class AqsModel(models.Model):
    model = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'aqs_model'
        verbose_name = 'Aqs Model'
        verbose_name_plural = 'Aqs Models'

    def __str__(self):
        return self.model

class AqsSystem(models.Model):
    serialno = models.CharField(max_length=15, primary_key=True)
    model = models.ForeignKey(AqsModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aqs_system'
        verbose_name = 'Aqs System'
        verbose_name_plural = 'Aqs Systems'

    def __str__(self):
        return f"{self.serialno} - {self.model}"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name
  
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.description

class MeasurementPoint(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   mp_type_id = models.IntegerField()
   description = models.CharField(max_length=255, null=True, blank=True)
   aq_unit_id = models.IntegerField()
   geo_xy = gis_models.PointField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
       managed = False
       db_table = 'measurement_pt'
       verbose_name = 'Measurement Point'
       verbose_name_plural = 'Measurement Points'

   def __str__(self):
        return self.name

class MeasurementPointEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    ts = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=255, null=True, blank=True)
    measurement_pt_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'measurement_pt_event'
        verbose_name = 'Measurement Point Event'
        verbose_name_plural = 'Measurement Point Events'

    def __str__(self):
        return f"Event ID: {self.id}, Measurement Point ID: {self.measurement_pt_id}"

class MeasurementPointHistory(models.Model):
    event_date = models.DateTimeField(primary_key=True, default=timezone.now)
    old_sensor_id = models.IntegerField(null=True, blank=True)
    measurement_pt_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'measurement_pt_history'
        verbose_name = 'Measurement Point History'
        verbose_name_plural = 'Measurement Point Histories'

    def __str__(self):
        return f"Event Date: {self.event_date}, Measurement Point ID: {self.measurement_pt_id}"
    
class MeasurementPointSensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    measurement_pt_id = models.IntegerField()
    sensor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'measurement_pt_sensor'
        verbose_name = 'Measurement Point Sensor'
        verbose_name_plural = 'Measurement Point Sensors'
        unique_together = ['measurement_pt_id', 'sensor_id']

    def __str__(self):
        return f"Measurement Point ID: {self.measurement_pt_id}, Sensor ID: {self.sensor_id}"
    
class MeasurementPointType(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100, null=False)

    class Meta:
        managed = False
        db_table = '"aqs"."measurement_pt_type"'
        verbose_name = 'Measurement Point Type'
        verbose_name_plural = 'Measurement Point Types'

    def __str__(self):
        return self.description

class Measurement(models.Model):
    ts = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(null=True)
    measurement_pt_id = models.IntegerField(primary_key=True)
    tag_id = models.IntegerField()
    sensor_id = models.IntegerField()
    offset_applied = models.FloatField(default=0.0)
    scale_applied = models.FloatField(default=1.0)

    class Meta:
        managed = False
        db_table = '"aqs"."measurement"'
        verbose_name = 'measurement'
        verbose_name_plural = 'measurements'
        unique_together = ['ts', 'sensor_id', 'tag_id']

    def __str__(self):
        return f"ts : {self.ts}, Sensor ID : {self.sensor_id}, Tag ID : {self.tag_id}"

class OEMManufacturer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'oem_manufacturer'
        verbose_name = 'OEM Manufacturer'
        verbose_name_plural = 'OEM Manufacturers'

    def __str__(self):
        return self.name
    
class Site(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    addr_street = models.CharField(max_length=100, null=True, blank=True)
    addr_postcode = models.CharField(max_length=10, null=True, blank=True)
    addr_city = models.CharField(max_length=100, null=True, blank=True)
    #geo_xy = gis_models.PointField(null=True, blank=True)
    def get_geo_xy(self):
        if self.geo_xy:
            x, y = eval(self.geo_xy)
            return Point(x, y)
        else:
            return None
    created_at = models.DateTimeField(auto_now_add=True)
    site_operator_id = models.IntegerField()
    site_owner_id = models.IntegerField()
    owner_parent_id = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = '"aqs"."site"'
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
        unique_together = ['id']

    def __str__(self):
        return self.name
    
class Plant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    site_id = models.IntegerField()
    geo_xy = gis_models.PointField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'plant'
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

    def __str__(self):
        return self.name
    
class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    serialno = models.CharField(max_length=100)
    sensor_type_id = models.IntegerField()
    aqs_system_serialno = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'sensor'
        verbose_name = 'Sensor' 
        verbose_name_plural = 'Sensors'

    def __str__(self):
        return self.serialno

class SensorHistory(models.Model):
    ts = models.DateTimeField(primary_key=True)
    event_id = models.IntegerField()
    description = models.CharField(max_length=255, null=True, blank=True)
    sensor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensor_history'
        verbose_name = 'Sensor History'
        verbose_name_plural = 'Sensor Histories'

    def __str__(self):
        return f"{self.ts} - {self.sensor_id}"

class SensorType(models.Model):
    description = models.CharField(max_length=100)
    part_no = models.CharField(max_length=50)
    part_no_oem = models.CharField(max_length=50, null=True, blank=True)
    oem_mfr_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensor_type'
        verbose_name = 'Sensor Type'
        verbose_name_plural = 'Sensor Types'

    def __str__(self):
        return self.description

class SensorVerification(models.Model):
    ts = models.DateTimeField(primary_key=True)
    offset = models.FloatField(null=True, blank=True)
    factor = models.FloatField(null=True, blank=True)
    tag_id = models.IntegerField(null=True, blank=True)
    sensor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sensor_verification'
        verbose_name = 'Sensor Verification'
        verbose_name_plural = 'Sensor Verifications'

    def __str__(self):
        return f"Sensor Verification - {self.ts}"



# class Site(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     addr_street = models.CharField(max_length=100, null=True, blank=True)
#     addr_postcode = models.CharField(max_length=10, null=True, blank=True)
#     addr_city = models.CharField(max_length=100, null=True, blank=True)
#     geo_xy = gis_models.PointField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     site_operator = models.ForeignKey('Operator', on_delete=models.CASCADE)
#     site_owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
#     owner_parent = models.ForeignKey('Owner', null=True, blank=True, related_name='child_sites', on_delete=models.SET_NULL)

#     class Meta:
#         managed = False
#         db_table = 'site'
#         verbose_name = 'Site'
#         verbose_name_plural = 'Sites'

#     def __str__(self):
#         return self.name

class SiteContact(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=254)
    mobile_phone = models.CharField(max_length=20, null=True, blank=True)
    work_phone = models.CharField(max_length=20, null=True, blank=True)
    comment = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='contacts')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'site_contact'
        verbose_name = 'Site Contact'
        verbose_name_plural = 'Site Contacts'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class TagName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255)
    unit_long = models.CharField(max_length=255, null=True, blank=True)
    unit_description = models.CharField(max_length=255, null=True, blank=True)
    tag_type_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'tag_name'
        verbose_name = 'Tag Name'
        verbose_name_plural = 'Tag Names'

    def __str__(self):
        return self.name

class AQUnit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    plant_id = models.IntegerField()
    aq_unit_type_id = models.IntegerField()
    description = models.CharField(max_length=255, null=True, blank=True)
    geo_xy = gis_models.PointField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = '"aqs"."aq_unit"'
        verbose_name = 'aqs.aq_unit'
        verbose_name_plural = 'aqs.aq_units'

    def __str__(self):
        return f"{self.id}, {self.name}, {self.plant_id}, {self.aq_unit_type_id}"

class AQUnitType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'aq_unit_type'
        verbose_name = 'aqs.aq_unit_type'
        verbose_name_plural = 'aqs.aq_unit_types'

    def __str__(self):
        return self.type

class MqttTopic(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'mqtt_topic'
        verbose_name = 'MQTT Topic'
        verbose_name_plural = 'MQTT Topics'

    def __str__(self):
        return self.topic

class LoggerConfig(models.Model):
     mqtt_topic_id = models.IntegerField(primary_key=True) 
     tag_name_id = models.IntegerField() 
     sensor_id = models.IntegerField()
     log_interval_sec = models.IntegerField() 
     log_on_change = models.BooleanField(default=False) 
     logger_id = models.IntegerField()
     
     class Meta:
         managed = False
         db_table = '"aqs"."logger_config"'
         unique_together = ['mqtt_topic_id', 'sensor_id', 'tag_name_id'] 
         verbose_name = 'Logger Configuration'
         verbose_name_plural = 'Logger Configurations' 
    
class VersionInfo(models.Model):
    id = models.AutoField(primary_key=True)
    schema_version = models.TextField(default='0.7', null=False)
    schema_updated = models.DateTimeField(default=timezone.now, null=False)

    class Meta:
        managed = False
        db_table = 'version_info'
        verbose_name = 'Version Information'
        verbose_name_plural = 'Version Information'

    def __str__(self):
        return f'{self.schema_version} - {self.schema_updated}'
    
class TagType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255, null=False)

    class Meta:
        managed = False
        db_table = 'tag_type'
        verbose_name = 'Tag Type'
        verbose_name_plural = 'Tag Types'

    def __str__(self):
        return self.type

class LoggerInstance(models.Model):
    name = models.TextField(null=False)

    class Meta:
        managed = False
        db_table = 'logger_instance'
        verbose_name = 'Logger Instance'
        verbose_name_plural = 'Logger Instances'

    def __str__(self):
        return self.name
    
