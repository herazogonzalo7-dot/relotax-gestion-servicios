from django import forms #Importación del módulo forms de Django
from .models import Abonado #Como el formulario está ligado a una BD, se importa el modelo Abonado (tabla Abonado)

class AbonadoForm(forms.ModelForm): #Formulario AbonadoForm, se usa la clase ModelForm (dentro de forms) para facilitar la creación del formulario utilizando como plntilla las columnas del modelo
    class Meta: #Metadatos
        model = Abonado #Modelo de la BD
        fields = ['nombre', 'domicilio', 'localidad', 'fecha_ingreso', 'contacto', 'telefono', 'comentarios'] #Lista que contiene los nombres exactos de las columnas del modelo Abonado que se van a mostrar en el formulario
        widgets = { #Diccionario de Python que le indica a Django que se van a cambiar la apariencia visual de varios campos del formulario
            #Para cada campo del formulario, se usan 2 diccionarios para cada campo, para poder aplicarle estilos al formulario en su conjunto.
            #forms.TextInput trae desde forms una clase que dibuja el campo como una caja de texto simple.
            #attrs (abreviatura de atributo), es un diccionario que esteblece como atributo form-control, un estilo CSS de Bootstrap, placeholder define un texto gris de fondo.
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localidad'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Persona de contacto'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones opcionales'}),
        }