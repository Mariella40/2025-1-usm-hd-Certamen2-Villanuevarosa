from django.urls import path
from . import views

app_name = 'MisComunas'

urlpatterns = [
    path('', views.listar_comunas, name='listar'),
    path('nueva/', views.crear_comuna, name='crear'),
    path('<int:id>/editar/', views.editar_comuna, name='editar'),
    path('<int:id>/eliminar/', views.eliminar_comuna, name='eliminar'),
]
