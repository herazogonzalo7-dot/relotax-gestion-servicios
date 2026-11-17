from django.shortcuts import render, redirect #Desde django, accede al módulo shortcuts e importa las funciones render y redirect
from django.contrib import messages #Desde django, accede al módulo contrib e importa el sistema messages (mensajes) 
from .forms import AbonadoForm #Desde l archivo forms importa el formulario AbonadoForm

#Función que manejará toda la lógica para dar de alta un nuevo abonado. Desde la visualización del formulario vacío (método GET, es decir mostrar), como así también el procesamiento y guardado de los datos enviados por el usuario (método POST, es decir enviar)
def alta_abonado(request):
    #Si el usuario envió el formulario completado (es decir que hizo click en guardar)
    if request.method == 'POST':
        #Carga los datos que viajaron en la petición POST dentro del formulario
        formulario = AbonadoForm(request.POST)
        #Si el formulario es válido, es decir si se validan todos los campos según las reglas establecidas en el modelo y en el form
        if formulario.is_valid():
            #Guarda automáticamente los datos que se validaron, en la base de datos postgreSQL
            formulario.save()
            #Haciendo uso del sistema messages, muestra un mensaje de confirmación cuando se realizó una nueva carga exitosa
            messages.success(request, '¡El abonado fue registrado con éxito en el sistema!')
            #Redirección a la misma página para continuar cargando
            return redirect('alta_abonado')
    #Pero si el usuario entra a la página por primera vez, se le muestra el formulario vacío
    else:
        formulario = AbonadoForm()
    
    #Se envia la variable formulario, contenida dentro de la etiqueta 'form', a alta_abonado, así pueda recibir el formulario y aplicarle estilos con CSS/ Bootstrap 
    #Se empaqueta la variable formulario bajo la etiqueta 'form' y se envía a la plantilla HTML (alta_abonado.html). Cuando este archivo HTML recibe la variable la dibuja en pantalla integrandola con los estilos CSS y de Bootstrap
    return render(request, 'gestion_abonados/alta_abonado.html', {'form': formulario})


    
    