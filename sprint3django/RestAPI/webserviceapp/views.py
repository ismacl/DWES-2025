from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tpeliculas

def pagina_de_prueba(request):
    return HttpResponse("<h1>Hola caracola</h1>")

def devolver_peliculas(request):
	lista = Tpeliculas.objects.all()
	respuesta_final = []
	for fila_sql in lista:
		diccionario = {}
		diccionario['id'] = fila_sql.id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['url_imagen'] = fila_sql.url_imagen
		diccionario['director'] = fila_sql.director
		diccionario['año_estreno'] = fila_sql.año_estreno
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

def devolver_pelicula_por_id(request, id_solicitado):
	pelicula = Tpeliculas.objects.get(id = id_solicitado)
	comentarios = pelicula.tcomentarios_set.all()
	lista_comentarios = []
	for fila_comentario_sql in comentarios:
		diccionario = {}
		diccionario['pelicula_id'] = fila_comentario_sql.pelicula_id
		diccionario['comentario'] = fila_comentario_sql.comentario
		lista_comentarios.append(diccionario)
	resultado = {
		'pelicula_id': pelicula.id,
		'titulo': pelicula.nombre,
		'url_imagen':pelicula.url_imagen,
		'duracion_h':pelicula.director,
		'desarolladora':pelicula.año_estreno,
		'comentarios':lista_comentarios
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})