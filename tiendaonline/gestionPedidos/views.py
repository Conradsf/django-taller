from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articles
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import contact_form

# Create your views here.

def search_products(request):

  return render(request, "search_products.html")

def search_results(request):

  if request.GET["prd"]:
    # Comprobación de que el formulario funciona:
    # msg="Founded Articles: %r" %request.GET["prd"]

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

def contact(request):

  if request.method=="POST":

    form=contact_form(request.POST)

    if form.is_valid():

      valid_form=form.cleaned_data

      send_mail(valid_form['subject'], valid_form['message'],
      valid_form.get('email',''),['conradsf@gmail.com'],)

      return render(request, "thanks.html")

  else:

    form=contact_form()

  return render(request, "contact2.html", {"form":contact_form})

  """
  Forma rudimentaria de hacer un formulario:

    subject=request.POST["subject"]
    message=request.POST["message"] + " " + request.POST["email"]
    email_from=settings.EMAIL_HOST_USER
    recipient_list=["conradsf@gmail.com"]
    
    send_mail(subject, message, email_from, recipient_list)
    
    return render(request, "thanks.html")

  return render(request, "contact.html")
  """