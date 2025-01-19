from django.contrib import admin
from import_export import resources
from .models import Records, configuration
from import_export.admin import ExportMixin  # Importa ExportMixin

# Crear un recurso de exportación para Records
class RecordsResource(resources.ModelResource):
    class Meta:
        model = Records

class ConfigurationibResource(resources.ModelResource):
    class Meta:
        model = configuration

# Crear una clase ModelAdmin personalizada con la opción de exportar
class RecordsAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'humidity1', 'temperature1', 'humidity2', 'temperature2', 'humidity_average', 'temperature_average', 'timestamp')
    list_per_page = 20
    search_fields = ('id', 'timestamp')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
    
    resource_class = RecordsResource  # Asocia el recurso de exportación

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('sampling_time', 'temperature_min_1', 'temperature_max_1', 'humidity_min_1', 'humidity_max_1', 'temperature_min_2', 'temperature_max_2', 'humidity_min_2', 'humidity_max_2', 'temperature_min_alert', 'temperature_max_alert', 'humidity_min_alert', 'humidity_max_alert')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# Registra el modelo en el admin
admin.site.register(Records, RecordsAdmin)
admin.site.register(configuration, ConfigurationAdmin)