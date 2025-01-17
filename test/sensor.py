import time
import board
import adafruit_ahtx0
import psycopg2
from psycopg2 import sql
from datetime import datetime


# Configuración de la conexión a la base de datos
DB_CONFIG = {
    'dbname': 'humiditycontrol',
    'user': 'django_user',
    'password': 'Krs_1q%qt-t2W',
    'host': 'localhost',
    'port': '5432'
}

def insert_reading(humidity, temperature):
    """Inserta una lectura de humedad y temperatura en la tabla test_sensor1."""
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Consulta para insertar los datos
        insert_query = sql.SQL("""
            INSERT INTO dashboard_records (humidity1, temperature1, humidity2, temperature2, humidity3, temperature3, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """)
        cursor.execute(insert_query, (humidity, temperature, humidity, temperature, humidity, temperature, datetime.now()))

        # Confirmar los cambios
        connection.commit()
        print("Registro guardado exitosamente.")
    except Exception as e:
        print("Error al guardar el registro:", e)
    finally:
        # Cerrar conexión
        if connection:
            cursor.close()
            connection.close()

# Crear objeto del sensor, comunicándose con el bus I2C predeterminado
i2c = board.I2C()  # Usa board.SCL y board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

# Bucle principal para tomar lecturas y almacenarlas
try:
    while True:
        # Leer datos del sensor
        temperature = round(sensor.temperature, 2)
        humidity = round(sensor.relative_humidity, 2)

        # Mostrar lecturas en la terminal
        print("\nTemperature: %0.1f C" % temperature)
        print("Humidity: %0.1f %%" % humidity)

        # Guardar lecturas en la base de datos
        insert_reading(humidity, temperature)

        # Esperar 2 segundos antes de la siguiente lectura
        time.sleep(30)
except KeyboardInterrupt:
    print("Ejecución interrumpida por el usuario.")
