import time
import board
import adafruit_ahtx0
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Configuración de la conexión a la base de datos
DB_CONFIG = {
    'dbname': 'humidity_temperature_control',
    'user': 'django_user',
    'password': 'Krs_1q%qt-t2W',
    'host': 'localhost',
    'port': '5432'
}

def insert_reading(humidity1, temperature1, humidity2, temperature2, humidity_avg, temperature_avg):
    """Inserta una lectura de humedad y temperatura en la tabla dashboard_records."""
    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Consulta para insertar los datos
        insert_query = sql.SQL("""
            INSERT INTO dashboard_records (humidity1, temperature1, humidity2, temperature2, humidity_average, temperature_average, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """)
        # Insertar los valores con la marca de tiempo actual
        cursor.execute(insert_query, (
            humidity1, temperature1,
            humidity2, temperature2,
            humidity_avg, temperature_avg,
            datetime.now()
        ))

        # Confirmar los cambios
        connection.commit()
        print("Registro guardado exitosamente en la base de datos.")
    except Exception as e:
        print("Error al guardar el registro:", e)
    finally:
        # Cerrar conexión
        if connection:
            cursor.close()
            connection.close()

def get_sampling_time_from_db():

    try:
        # Conexión a la base de datos
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Consulta SQL para obtener el tiempo de muestreo
        cursor.execute("SELECT sampling_time FROM dashboard_configuration LIMIT 1;")
        result = cursor.fetchone()

        if result:
            time_mapping = {
                '15S': 15,   # 5 minutos en segundos
                '30S': 30,   # 5 minutos en segundos
                '1M': 60,   # 5 minutos en segundos
                '5M': 300,   # 5 minutos en segundos
                '10M': 600,  # 10 minutos en segundos
                '30M': 1800, # 30 minutos en segundos
                '1H': 3600,  # 1 hora en segundos
                '2H': 7200   # 2 horas en segundos
            }
            sampling_time = result[0]
            return time_mapping.get(sampling_time, 300)  # Valor por defecto: 5 minutos
        else:
            print("No se encontró ninguna configuración en la tabla. Usando valor por defecto.")
            return 300  # Valor por defecto

    except Exception as e:
        print(f"Error al obtener el tiempo de muestreo desde la base de datos: {e}")
        return 300  # Valor por defecto

    finally:
        # Cerrar la conexión
        if connection:
            cursor.close()
            connection.close()


# Inicializar el bus I2C
i2c = board.I2C()

# Crear instancias para cada sensor en sus direcciones respectivas
sensor1 = adafruit_ahtx0.AHTx0(i2c, address=0x38)
sensor2 = adafruit_ahtx0.AHTx0(i2c, address=0x39)

try:
    while True:
        # Leer datos del primer sensor
        temperature1 = round(sensor1.temperature, 2)
        humidity1 = round(sensor1.relative_humidity, 2)

        # Leer datos del segundo sensor
        temperature2 = round(sensor2.temperature, 2)
        humidity2 = round(sensor2.relative_humidity, 2)

        # Calcular promedios
        temperature_avg = round((temperature1 + temperature2) / 2, 2)
        humidity_avg = round((humidity1 + humidity2) / 2, 2)

        # Mostrar lecturas en la pantalla
        print(f"Sensor 1 - Temperature: {temperature1}°C, Humidity: {humidity1}%")
        print(f"Sensor 2 - Temperature: {temperature2}°C, Humidity: {humidity2}%")
        print(f"Averages - Temperature: {temperature_avg}°C, Humidity: {humidity_avg}%")

        # Guardar lecturas en la base de datos
        insert_reading(humidity1, temperature1, humidity2, temperature2, humidity_avg, temperature_avg)
        sampling_time = get_sampling_time_from_db()
        print(f"Esperando {sampling_time} segundos para la próxima muestra...")
        time.sleep(sampling_time)

        # Esperar 30 segundos antes de la siguiente lectura
        # time.sleep(30)

except KeyboardInterrupt:
    print("\nEjecución interrumpida por el usuario.")
except Exception as e:
    print(f"Error: {e}")
