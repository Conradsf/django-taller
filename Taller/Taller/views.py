from django.http import HttpResponse
# No hace falta importar Tamplate, Context si trabajamos con el import de loader
# 
# from django.template import  Template, Context
#
# para optimizar el import de loader se puede optimizar más importando solo el loader
# 
# from django.template import loader

from django.template.loader import get_template


class Car(object):
  def __init__(self, brand, color, registration):
    self.brand=brand
    self.color=color
    self.registration=registration

def Formulario(request):

  # Forma poco convencional de cargar un template sin usar settings.py:
  # ANTES
  # doc_externo=open("/mnt/d/021 Proyectos Programacion/django/Taller/Taller/Templates/miplantilla.html")
  # plt=Template(doc_externo.read())
  # doc_externo.close()
  
  # No hace falta usar el loader si lo importamos desde inicio:
  # ANTES usamos loader.
  # AHORA si importamos el método directamente no hace falta poner loader.
  # doc_externo=loader.get_template('miplantilla.html')
  
  # No hace falta usar el método Context cuando usamos Loader. 
  # ANTES
  # AHORA En vez de eso directamente pasamos el dict.
  # ctx=Context({"marca": car1.brand, "color": car1.color, "matricula": car1.registration, "temas":taller_temas})

  # el objeto ctx tiene un formato distinto cuando usas el método Template() y loader.get_template().
  # ANTES usamos el Context() para enviar los argumentos al render
  # AHORA solo pasamos el dict.
  # documento=plt.render(ctx)

  doc_externo=get_template('miplantilla.html')
  car1 = Car("Seat","Blue","4321ABC")
  taller_temas = ["Plantillas","Modelos","Formulario"]
  args = {"marca": car1.brand, "color": car1.color, "matricula": car1.registration, "temas":taller_temas}
  documento=doc_externo.render(args)
  return HttpResponse(documento)

def Resultado(request):
  return HttpResponse("Página resultado de consulta")

