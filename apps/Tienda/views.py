
# Create your views here.

from django.shortcuts import render,redirect
from .models import *
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def cargarInicio(request):
    productos = Producto.objects.all()
    cate_perros = Producto.objects.filter(categoria_id = 1)
    cate_gatos = Producto.objects.filter(categoria_id = 2)
    return render(request, "inicio.html",{"prod":productos, "cate_perro":cate_perros,"cate_gato":cate_gatos})


@login_required
def cargarAgregarProducto(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request,"agregar.html",{"cate":categorias, "prod":productos})


@login_required
def agregarProducto(request):
    #print("AGREGAR PRODUCTO",request.POST)
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_image = request.FILES['txtImg']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku, nombre= v_nombre, descripcion = v_descripcion, stock = v_stock,precio = v_precio,fecha_vencimiento = v_fecha_vencimiento, image_url = v_image, categoria_id = v_categoria )

    return redirect('/agregar')




@login_required
def cargarEditarProducto(request,sku):
    productos = Producto.objects.get(sku = sku)
    categorias = Categoria.objects.all()

    cateId = productos.categoria_id

    productoCategoria = Categoria.objects.get(categoria_id = cateId.categoria_id).categoria_id

    return render(request,"editarProducto.html",{"prod":productos, "cate":categorias,"categoriaId":productoCategoria})


@login_required
def editarProductoForm(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(sku = v_sku)
    v_nombre = request.POST['txtNombre']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']
    v_precio = request.POST['txtPrecio']
    if request.POST['fechaVencimientoSel'] == "":
        v_fecha_vencimiento = None
    else:
        v_fecha_vencimiento = request.POST['fechaVencimientoSel']
    v_categoria = Categoria.objects.get(categoria_id = request.POST['cmbCategoria'])


    try:
        v_image = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.image_url))
        os.remove(ruta_imagen)
    except:
        v_image = productoBD.image_url


    productoBD.nombre = v_nombre
    productoBD.descripcion = v_descripcion
    productoBD.stock = v_stock
    productoBD.precio = v_precio
    productoBD.fecha_vencimiento = v_fecha_vencimiento
    productoBD.image_url = v_image
    productoBD.categoria_id = v_categoria


    productoBD.save()
    return redirect('/agregar')

@login_required
def eliminarProducto(request,sku):
    print("ELIMINAR PRODUCTO",sku)
    producto = Producto.objects.get(sku = sku)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.image_url))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/agregar')

def cargarClima(request):
    return render(request,"Clima.html")

def cargarComentarios(request):
    return render(request,"Comentarios.html")

def cargarSignup(request):
    if request.method == 'GET':
        return render(request, "signup.html",{
        'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            #registrar usuario
            try:
                user=User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('/agregar')
            except IntegrityError:
                return render(request, "signup.html",{
                'form':UserCreationForm,
                'error':'Usuario ya existe'
                })
        return render(request, "signup.html",{
                'form':UserCreationForm,
                'error':'Contraseñas no coinciden'
                })
        
        
def signout(request):
    logout(request) 
    return redirect('inicio') 


def signin(request):
    if request.method =='GET':
        return render(request,'signin.html',{
        'form':AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
            'form':AuthenticationForm,
            'error': 'Nombre o contraseña incorrecta'
        })
        else:
            login(request,user)
            return redirect('/agregar')
            
            
            
            
def cargarDespachos(request):
    render(request,"Despacho.html")
    
    
    
def cargarSuscripcion(request):
    render(request,"suscripcion.html")
        
    

        
        
        
        
