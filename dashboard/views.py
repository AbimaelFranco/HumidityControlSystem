from django.shortcuts import render
from django.utils.timezone import now, timedelta, localtime
from django.core.paginator import Paginator
from dashboard.models import Records

def dashboard_home(request):
    # Obtener registros de las últimas 24 horas
    last_24_hours = now() - timedelta(hours=24)
    records = Records.objects.filter(timestamp__gte=last_24_hours)
    records = records[::-1]

    # Organizar datos para la gráfica y convertir de Decimal a float
    timestamps = [localtime(record.timestamp).strftime("%H:%M") for record in records]  # Convertir a zona horaria local
    
    # Convertir a float para evitar problemas con los tipos Decimal
    humidity1 = [float(record.humidity1) for record in records]
    temperature1 = [float(record.temperature1) for record in records]
    humidity2 = [float(record.humidity2) for record in records]
    temperature2 = [float(record.temperature2) for record in records]

    # Valores promedio
    avg_humidity = [float(record.humidity_average) for record in records]
    avg_temperature = [float(record.temperature_average) for record in records]

     # Obtener el último registro
    last_record = records[-1]

    # Obtener los últimos valores de temperatura, humedad y la hora
    last_timestamp = localtime(last_record.timestamp).strftime("%H:%M")
    last_avg_humidity = float(last_record.humidity_average)
    last_avg_temperature = float(last_record.temperature_average)


    context = {
        'timestamps': timestamps,
        'humidity1': humidity1,
        'temperature1': temperature1,
        'humidity2': humidity2,
        'temperature2': temperature2,
        'avg_humidity': avg_humidity,
        'avg_temperature': avg_temperature,
        'last_timestamp': last_timestamp,
        'last_avg_humidity': last_avg_humidity,
        'last_avg_temperature': last_avg_temperature,
    }
    
    # Enviar los datos al template
    return render(request, 'dashboard/home.html', context)

def graphs(request):
    # Obtener registros de las últimas 24 horas
    last_24_hours = now() - timedelta(hours=24)
    records = Records.objects.filter(timestamp__gte=last_24_hours)
    records = records[::-1]

    # Organizar datos para la gráfica y convertir de Decimal a float
    timestamps = [localtime(record.timestamp).strftime("%H:%M") for record in records]  # Convertir a zona horaria local
    
    # Convertir a float para evitar problemas con los tipos Decimal
    humidity1 = [float(record.humidity1) for record in records]
    temperature1 = [float(record.temperature1) for record in records]
    humidity2 = [float(record.humidity2) for record in records]
    temperature2 = [float(record.temperature2) for record in records]

    # Valores promedio
    avg_humidity = [float(record.humidity_average) for record in records]
    avg_temperature = [float(record.temperature_average) for record in records]

     # Obtener el último registro
    last_record = records[-1]

    # Obtener los últimos valores de temperatura, humedad y la hora
    last_timestamp = localtime(last_record.timestamp).strftime("%H:%M")
    last_avg_humidity = float(last_record.humidity_average)
    last_avg_temperature = float(last_record.temperature_average)


    context = {
        'timestamps': timestamps,
        'humidity1': humidity1,
        'temperature1': temperature1,
        'humidity2': humidity2,
        'temperature2': temperature2,
        'avg_humidity': avg_humidity,
        'avg_temperature': avg_temperature,
        'last_timestamp': last_timestamp,
        'last_avg_humidity': last_avg_humidity,
        'last_avg_temperature': last_avg_temperature,
    }
    
    # Enviar los datos al template
    return render(request, 'dashboard/graphs.html', context)

def registers(request):
    registros = Records.objects.all().order_by('timestamp')  # Ordenar por fecha y hora descendente
    paginator = Paginator(registros, 20)  # 20 registros por página

    page_number = request.GET.get('page')  # Obtener el número de página desde los parámetros de la URL
    page_obj = paginator.get_page(page_number)  # Obtener la página actual

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'dashboard/registers.html', context)