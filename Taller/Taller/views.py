from django.http import HttpResponse
from django.template import Template, Context

def Formulario(request):
  doc_externo=open("/mnt/d/021 Proyectos Programacion/django/Taller/Taller/Templates/miplantilla.html")
  plt=Template(doc_externo.read())
  doc_externo.close()
  ctx=Context()
  documento=plt.render(ctx)
  return HttpResponse(documento)

def Resultado(request):
  return HttpResponse("Página resultado de consulta")

