# myapp/models.py
from django.db import models

class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    serialno = models.CharField(max_length=100)
    sensor_type_id = models.IntegerField()
    aqs_system_serialno = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'aqs.sensor'
        verbose_name = 'Sensor' 
        verbose_name_plural = 'Sensors'

    def __str__(self):
        return self.serialno
