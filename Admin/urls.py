from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('materias/', views.materias, name='materias'),
    path('docentes/', views.docentes, name='docentes'),
    path('mensajes_bot/', views.mensajes_bot, name='mensajes_bot'),
    path("mensajes_search/", views.search_mensajes_bot, name="mensajes_search"),
    path('resumen/', views.resumen, name='resumen'),
    path('mensajes/', views.mensajes, name='mensajes'), 
    path('reportes/', views.reportes, name='reportes'),
    path('programar_tarea/', views.programar_tarea, name='programar_tarea'),
    path('tareas_programadas/', views.tareas_programadas, name='tareas_programadas'),
    path('anuncios_programados/', views.anuncios_programados, name='anuncios_programados'),
    path('addbot/', views.addbot, name='addbot'),
    path("BotView/", views.BotView, name="BotView"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("materias/", views.materias, name="materias")
]