from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Productos
 
from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms
from django.http import HttpResponse


#vista inicial.
class home(TemplateView):
    template_name = 'general/base.html'

class ProductosListado(ListView): 
    model = Productos
    template_name = 'general/productos.html'

class ProductosDetalle(DetailView): 
    model = Productos
 
class ProductosCrear(SuccessMessageMixin, CreateView): 
    model = Productos
    form = Productos
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Productos  
    template_name = "general/crear.html"  
 
    # Redireccionamos a la página principal luego de crear un registro o Productos
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ProductosActualizar(SuccessMessageMixin, UpdateView): 
    model = Productos
    form = Productos
    fields = "__all__"  
    success_message = 'Productos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Productos 
 
    # Redireccionamos a la página principal luego de actualizar un registro o Productos
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 
 
class ProductosEliminar(SuccessMessageMixin, DeleteView): 
    model = Productos 
    form = Productos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Productos
    def get_success_url(self): 
        success_message = 'Productos Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Productos 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'