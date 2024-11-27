from django.contrib import admin
from django.urls import path

from webserviceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', views.pagina_de_prueba),
    path('peliculas', views.devolver_peliculas),
    path('peliculas/<int:id_solicitado>', views.devolver_pelicula_por_id)
]
