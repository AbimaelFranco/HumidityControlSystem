#!/bin/bash
cd /home/camara/Desktop/proyecto/HumidityControlSystem
source env/bin/activate  # Activa el entorno virtual
python scripts/sensors.py &
python manage.py runserver 0.0.0.0:8000
