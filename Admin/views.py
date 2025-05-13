from django.shortcuts import render
from Admin.models import *
from django.db.models import Q
from datetime import datetime

def dashboard(request):
    return render(request, "admin/dashboard.html")

def estudiantes(request):
    return render(request, "admin/estudiantes.html")

def materias(request):
    return render(request, "admin/materias.html")

def docentes(request):
    return render(request, "admin/docentes.html")

def mensajes_bot(request):
    mensajes = Solicitud_Bot.objects.all()
    return render(request, "admin/mensajes_bot.html", {'mensajes': mensajes} )
def search_mensajes_bot(request):
    mensaje = request.GET.get("mensaje", "").strip()  
    if not mensaje:  
        mensajes = Solicitud_Bot.objects.all()  
    else:
        palabras = mensaje.split()
        query = Q()
        for palabra in palabras:
            query |= Q(Consulta__icontains=palabra)
        try:
            mensajes = Solicitud_Bot.objects.filter(query)
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            mensajes = []
    return render(request, "admin/mensajes_bot.html", {"mensajes": mensajes, "mensaje_busqueda": mensaje})

def mensajes_date_search(request):
    inicio = request.GET.get("Inicio")
    final = request.GET.get("Final")
    
    try:
        inicio_date = datetime.strptime(inicio, "%Y-%m-%d") 
        final_date = datetime.strptime(final, "%Y-%m-%d")    
    except ValueError:
        inicio_date = final_date = None
    
    if inicio_date and final_date:
        mensajes = Solicitud_Bot.objects.filter(created_at__lte=final_date, created_at__gt=inicio_date)
    else:
        mensajes = Solicitud_Bot.objects.none()  
    
    return render(request, "admin/mensajes.html", {"mensajes": mensajes})


def resumen(request):
    return render(request, "admin/resumen.html")

def mensajes(request):
    return render(request, "admin/mensajes.html")

def reportes(request):
    return render(request, "admin/reportes.html")

def programar_tarea(request):
    return render(request, "admin/programar_tarea.html")

def tareas_programadas(request):
    return render(request, "admin/tareas_programadas.html")

def anuncios_programados(request):
    return render(request, "admin/anuncios.html")

def addbot(request):
    bot = Bot.objects.first()
    return render(request, "admin/addbot.html", {'bot': bot})
def BotView(request):
    if request.method == "POST":
        nombre = request.POST.get("Nombre")
        token = request.POST.get("Token")
        numero = request.POST.get("Numero")

        if Bot.objects.exists():
            bot = Bot.objects.first() 
            bot.Nombre = nombre
            bot.Token = token
            bot.Numero = numero
            bot.save()
        else:
            bot = Bot.objects.create(
                Nombre=nombre,
                Token=token,
                Numero=numero
            )
            bot.save()
        return render(request, 'admin/addbot.html', {'bot':bot}  ) 

def usuarios(request):
    return render(request, 'admin/usuarios.html')

def materias(request):
    return render(request, "Admin/materias.html")