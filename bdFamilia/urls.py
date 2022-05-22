from django.urls import path
from bdFamilia import views


'''Se detallan las urls creadas
Cada path direcciona a una función específica
'''
urlpatterns = [
    path('bienvenida/', views.bienvenida),
    path('listar-familia/', views.listar_familia),
    path('agregar-miembro/<str:nombre>/<int:edad>/<str:fechaNacimiento>/', views.agregar_miembro),
]
