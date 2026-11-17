from django.db import models

class Abonado(models.Model):
    """"La clase Abonado representa una tabla en la Base de Datos postgreSQL. Se crea mediante ORM (manipular bases de datos mediante código de programación Python) y almacena los datos principales para el registro y control de un abonado"""

    #Campos obligatorios que permiten la rápida identificación de un abonado
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=150)
    localidad = models.CharField(max_length=100)

    #Campo de fecha de alta del abonado dentro del sistema
    fecha_ingreso = models.DateField()

    #Campos para datos de contacto y de comunicación con el abonado
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    #Campo no obligatorio que permite agregar notas adicionales o comentarios
    comentarios = models.TextField(blank=True, null=True)  

    #Método que permite la representación en cadena de caracteres del objeto. Retorna el nombre del abonado con su respectiva localidad para facilitar la identificación visual en el panel de administracipon de Django
    
    def __str__(self):
        return f"{self.nombre} ({self.localidad})"