from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Teventos, Treservas, Tcomentarios, Tusuarios

@csrf_exempt
def listar_eventos(request):
    eventos = Teventos.objects.all().select_related('organizador')
    data = [{
        "id": evento.id,
        "titulo": evento.titulo,
        "descripcion": evento.descripcion,
        "fecha_hora": evento.fecha_hora,
        "capacidad_maxima": evento.capacidad_maxima,
        "organizador": evento.organizador.first_name
    } for evento in eventos]
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        data = json.loads(request.body)
        organizador = get_object_or_404(Tusuarios, id=data["organizador"])
        if organizador.rol != 'organizador':
            return JsonResponse({"error": "No tienes permisos para crear eventos"}, status=403)
        evento = Teventos.objects.create(
            organizador=organizador,
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            fecha_hora=data["fecha_hora"],
            capacidad_maxima=data["capacidad_maxima"],
            imagen_url=data["imagen_url"]
        )
        return JsonResponse({"id": evento.id, "mensaje": "Evento creado"})

@csrf_exempt
def eliminar_evento(request, id):
    evento = get_object_or_404(Teventos, id=id)
    if request.user.rol != 'organizador':
        return JsonResponse({"error": "No tienes permisos para eliminar eventos"}, status=403)
    evento.delete()
    return JsonResponse({"mensaje": "Evento eliminado"})

@csrf_exempt
def listar_reservas(request):
    reservas = Treservas.objects.filter(usuario=request.user).select_related('evento', 'usuario')
    data = [{
        "id": reserva.id,
        "evento": reserva.evento.titulo,
        "usuario": reserva.usuario.first_name,
        "entradas": reserva.entradas,
        "estado": reserva.tipo
    } for reserva in reservas]
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_reserva(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usuario = get_object_or_404(Tusuarios, id=data["usuario"])
        evento = get_object_or_404(Teventos, id=data["evento"])
        reserva = Treservas.objects.create(
            usuario=usuario,
            evento=evento,
            entradas=data["entradas"],
            tipo='pendiente'
        )
        return JsonResponse({"id": reserva.id, "mensaje": "Reserva creada"})

@csrf_exempt
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Treservas, id=id)
    if request.user != reserva.usuario:
        return JsonResponse({"error": "No puedes cancelar reservas de otros usuarios"}, status=403)
    reserva.delete()
    return JsonResponse({"mensaje": "Reserva eliminada"})

@csrf_exempt
def listar_comentarios(request, evento_id):
    comentarios = Tcomentarios.objects.filter(evento_id=evento_id).select_related('usuario', 'evento')
    data = [{
        "id": comentario.id,
        "evento": comentario.evento.titulo,
        "usuario": comentario.usuario.first_name,
        "comentario": comentario.comentario
    } for comentario in comentarios]
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_comentario(request):
    if request.method == "POST":
        data = json.loads(request.body)
        usuario = get_object_or_404(Tusuarios, id=data["usuario"])
        evento = get_object_or_404(Teventos, id=data["evento"])
        comentario = Tcomentarios.objects.create(
            usuario=usuario,
            evento=evento,
            comentario=data["comentario"]
        )
        return JsonResponse({"id": comentario.id, "mensaje": "Comentario creado"})

@csrf_exempt
def login_usuario(request):
    data = json.loads(request.body)
    usuario = data.get("username")
    password = data.get("password")
    user = authenticate(username=usuario, password=password)
    if user:
        login(request, user)
        return JsonResponse({"mensaje": "Login exitoso"})
    return JsonResponse({"error": "Credenciales incorrectas"}, status=400)

@csrf_exempt
def registrar_usuario(request):
    data = json.loads(request.body)
    usuario = data.get("username")
    email = data.get("email")
    password = data.get("password")
    user = User.objects.create_user(username=usuario, email=email, password=password)
    if user:
        return JsonResponse({"mensaje": "Usuario registrado con éxito"})
    return JsonResponse({"error": "Registro fallido"}, status=400)
from django.shortcuts import render

# Create your views here.
