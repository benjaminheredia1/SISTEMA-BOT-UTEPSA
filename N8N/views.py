from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from Admin.models import * 
from django.middleware.csrf import get_token
import json
# Create your views here.

@csrf_exempt
def AddMessage(request): 
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            consulta = data.get('Consulta')
            respuesta = data.get('Respuesta')
            chat = data.get("Id_Chat")
            user = data.get("Usuario")
            bot = Bot.objects.first()
            if not bot:
                return JsonResponse({"ERROR": "No hay ningún bot registrado en la tabla Bots"}, status=400)
            usuario_tabla = Usuario.objects.filter(Id_Chat=chat).first()
            if usuario_tabla:
                usuario = usuario_tabla
            else:
                usuario = Usuario(Id_Chat = chat, Usuario = user)
                usuario.save()
            solicitud_bot = Solicitud_Bot( Consulta = consulta, Respuesta = respuesta, Id_Usuario = usuario, Id_Bot = bot )
            solicitud_bot.save()
            return JsonResponse({ "Response": "Save Consult"}, status = 200)
            
        except Exception as ex :
            return JsonResponse({
                "ERROR": str(ex)
            }, status = 300)
        
def getCSRF(request):
    token = get_token(request)
    return HttpResponse(token, content_type = "text/plain")