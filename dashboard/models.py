from django.db import models

class Records(models.Model):
    # Sensor 1 readings
    humidity1 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidity Sensor 1")
    temperature1 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature Sensor 1")
    
    # Sensor 2 readings
    humidity2 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidity Sensor 2")
    temperature2 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature Sensor 2")
    
    # Sensor 3 readings
    humidity3 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidity Sensor 3")
    temperature3 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature Sensor 3")
    
    # Timestamp
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
        ordering = ['-timestamp']  # Order records by the newest first

    def __str__(self):
        return f"Record {self.id} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
