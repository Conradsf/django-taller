from django.db import models

# para crear las tablas en la base de datos:

class Clients(models.Model):
  name=models.CharField(max_length=30)
  direction=models.CharField(max_length=50)
  email=models.EmailField()
  phone=models.CharField(max_length=7)

class Articles(models.Model):
  name=models.CharField(max_length=30)
  section=models.CharField(max_length=20)
  price=models.IntegerField()

class Orders(models.Model):
  number=models.IntegerField()
  date=models.DateField()
  delivered=models.BooleanField()

  # recuerda instalar psycopg2 para poder importar la libreria de sql
  # python3 manage.py makemigrations sirve para convertir las tablas del model a lenguaje sql
  # python3 manage.py migrate sirve para migrar (ejecutar) la query sql hacia la bbdd
  # python3 manage.py shell para acceder a la shell de la app

  # para rellenar datos:
  # 1- importar la tabla:
  # from gestionPedidos.models import Articles:
  # 
  # 2- guardar las entencia en una variable
  # art=Articles(name='moto', section='harley', price=3000)
  #
  # 3- enviar la sentencia sql a la bdd:
  # art.save()
  #
  # bonus: forma de hacerlo más rapido usando método create:
  # art=Articles.objects.create(name='bicicleta', section='btwin', price=100)
  #
  # 4- para actualizar datos solo hace falta elegir la variable y cambiar el valor:
  # art.price=95
  # no olvidar de hacer art.save() para actualizar.
  #
  # Eliminar fila: 
  # deleterow=Articles.objects.get(id=2)
  # deleterow.delete()
  #
  # Forma de hacer select * de un model:
  # lista=Articles.objects.all()
  # lista.query.__str__()