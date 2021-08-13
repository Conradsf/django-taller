from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articles
# Create your views here.

def search_products(request):

  return render(request, "search_products.html")

def search_results(request):

  if request.GET["prd"]:
    #Comprobación de que el formulario funciona:
    #msg="Founded Articles: %r" %request.GET["prd"]
    
    product=request.GET["prd"]

    if len(product)>20:
      msg="This text is too long"

    else: 
      articles=Articles.objects.filter(name__icontains=product) 
      # name__icontains funciona parecido a un like en SQL.
      # se podría utilizar name__contains. Pero la i sirve para todas las BBDD 
   
      return render(request, "search_results.html",{"articles":articles, "query":product})

  else:

    msg="You have not entered any words"
  
  return HttpResponse(msg)

