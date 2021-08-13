from django.contrib import admin
from gestionPedidos.models import Clients, Articles, Orders

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
  """
  Creando una clase usando el argumento admin.ModelAdmin, 
  permite mostrar las columnas que queramos en las tablas dentro
  del panel de administración.

  En este caso, se veran solo 3 de las 4 columnas (el email, no)
  """ 
  list_display=("name", "direction", "phone")


  """
  También se pueden añadir barras de búsqueda siguiendo los criterios 
  que se pasen por argumentos
  """
  search_fields=("name", "phone")

class ArticlesAdmin(admin.ModelAdmin):
  """
  Para crear ventana de filtros:
  """
  list_filter=("section",)

class OrdersAdmin(admin.ModelAdmin):
  """
  Para filtrar por fecha y ver migas de pan
  """
  list_display=("number", "date")
  list_filter=("date",) #filter
  date_hierarchy="date" #breadcrumbs


admin.site.register(Clients,ClientsAdmin) # pasar como argumento la clase
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Orders, OrdersAdmin)