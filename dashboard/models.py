from django.db import models

class Records(models.Model):
    # Sensor 1 readings
    humidity1 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidity Sensor 1")
    temperature1 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature Sensor 1")
    
    # Sensor 2 readings
    humidity2 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidity Sensor 2")
    temperature2 = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature Sensor 2")
    
    # Sensor 3 readings
    humidity_average = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Humidity Average")
    temperature_average = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperature Average")
    
    # Timestamp
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")

    class Meta:
        verbose_name = "Registros"
        verbose_name_plural = "Registros"
        ordering = ['timestamp']  # Order records by the newest first

    def __str__(self):
        return f"Records {self.id} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class configuration(models.Model):
    TIME_CHOICES = [
        ('5M', '5 minutos'),
        ('10M', '10 minutos'),
        ('30M', '30 minutos'),
        ('1H', '1 hora'),
        ('2H', '2 horas'),
    ]
    
    # Campos de configuración
    sampling_time = models.CharField(
        max_length=3, 
        choices=TIME_CHOICES, 
        default='5M', 
        verbose_name="Tiempo de muestreo"
    )
    temperature_min_1 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=21.00, 
        verbose_name="Temperatura Mínima Sensor 1"
    )
    temperature_max_1 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=25.00, 
        verbose_name="Temperatura Máxima Sensor 1"
    )
    humidity_min_1 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=95.00, 
        verbose_name="Humedad Mínima Sensor 1"
    )
    humidity_max_1 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=100.00, 
        verbose_name="Humedad Máxima Sensor 1"
    )
    temperature_min_2 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=21.00, 
        verbose_name="Temperatura Mínima Sensor 2"
    )
    temperature_max_2 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=25.00, 
        verbose_name="Temperatura Máxima Sensor 2"
    )
    humidity_min_2 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=95.00, 
        verbose_name="Humedad Mínima Sensor 2"
    )
    humidity_max_2 = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=100.00, 
        verbose_name="Humedad Máxima Sensor 2"
    )
    temperature_min_alert = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=21.00, 
        verbose_name="Temperatura Mínima Alerta"
    )
    temperature_max_alert = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=25.00, 
        verbose_name="Temperatura Máxima Alerta"
    )
    humidity_min_alert = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=95.00, 
        verbose_name="Humedad Mínima Alerta"
    )
    humidity_max_alert = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=100.00, 
        verbose_name="Humedad Máxima Alerta"
    )
    
    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return f"Configuration - Sampling: {self.get_sampling_time_display()}"
