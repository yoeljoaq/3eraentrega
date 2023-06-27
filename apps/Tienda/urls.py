from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarInicio, name="inicio"),
    path('agregar',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),

    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProductoForm),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('Clima',views.cargarClima),
    path('Comentarios',views.cargarComentarios),
    path('signup/',views.cargarSignup),
    path('logout/',views.signout,name='logout'),
    path('signin/',views.signin, name='signin'),
    path('Despacho',views.cargarDespachos, name="Despacho"),
    path('suscripcion',views.cargarSuscripcion)
    
]
