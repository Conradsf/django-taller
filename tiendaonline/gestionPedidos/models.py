from django.db import models

# para crear las tablas en la base de datos:

class Clients(models.Model):
  name=models.CharField(max_length=30)
  direction=models.CharField(max_length=50, verbose_name="La dirección") #cambia el nombre del campo dentro de admin panel.
  # tambien se podria escribir el nombre del campo de esta forma:
  # direction=models.CharField("La dirección", max_length=50) ¡OJO! no sirve para FK
  email=models.EmailField(blank=True, null=True) #para k sea un campo opcional
  phone=models.CharField(max_length=9)

  def __str__(self):
    return 'Nombre*: %s ; Dirección*: %s ; Email: %s ; Teléfono: %s' % (self.name, self.direction, self.email, self.phone)


class Articles(models.Model):
  name=models.CharField(max_length=30)
  section=models.CharField(max_length=20)
  price=models.IntegerField()

  def __str__(self):
    return 'El nombre es %s la sección es %s y el precio es %s' % (self.name, self.section, self.price)

class Orders(models.Model):
  number=models.IntegerField()
  date=models.DateField()
  delivered=models.BooleanField()


"""
  recuerda instalar psycopg2 para poder importar la libreria de sql
  python3 manage.py makemigrations sirve para convertir las tablas del model a lenguaje sql
  python3 manage.py migrate sirve para migrar (ejecutar) la query sql hacia la bbdd
  python3 manage.py shell para acceder a la shell de la app

  para rellenar datos:
  1- importar la tabla:
  from gestionPedidos.models import Articles:
  
  2- guardar las entencia en una variable
  art=Articles(name='moto', section='harley', price=3000)
  
  3- enviar la sentencia sql a la bdd:
  art.save()
  
  bonus: forma de hacerlo más rapido usando método create:
  art=Articles.objects.create(name='bicicleta', section='btwin', price=100)
  
  4- Actualizar
  para actualizar datos solo hace falta elegir la variable y cambiar el valor:
  art.price=95
  no olvidar de hacer art.save() para actualizar.
  
  5- Eliminar fila: 
  deleterow=Articles.objects.get(id=2)
  deleterow.delete()
  
  6- Consultas: 
  
  Forma de hacer select * de un model:
  lista=Articles.objects.all()
  lista.query.__str__()
  
  Forma de hacer select "x" where "x":
  Articles.objects.filter(section='btwin')

  Forma de hacer select "x" where "y = x" and "z = u"
  Articles.objects.filter(section='btwin', price=100)

  Forma de utilizar ">" "<" desdel shell:
  Articles.objects.filter(section='btwin', price__gte=90)
  Articles.objects.filter(section='btwin', price__lte=100)

  També es pot utilitzar __range per buscar articles entre 2 valors:
  Articles.objects.filter(section='btwin', price__range(90,100)

  Ordenar registres recuperats:
  Articles.objects.filter(section='btwin').order_by('price')
  """