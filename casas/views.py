from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Casa, Avatar, Review
from .forms import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
   return render(request, "casas/home.html")

def about(request):
    return render(request, "casas/about.html")

def como_funciona(request):
    return render(request, "casas/como_funciona.html")



#Búsqueda

@login_required
def casa_buscar(request):
    return render(request, "casas/casaBuscar.html") 

@login_required
def casa_buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        casas = Casa.objects.filter(menu__icontains=patron)
        contexto = {"casas": casas}
        return render(request, "casas/casas.html", contexto)
    contexto = {'titulo': 'No se ingreso nada a buscar'}
    return render (request, "casas/casas.html", contexto)



#Crear y modificar casas

class Casaslist(LoginRequiredMixin,ListView):
    model = Casa

class Casacreate(LoginRequiredMixin, CreateView):
    model = Casa
    fields = ['calle' , 'altura', 'piso', 'departamento', 'localidad', 'horario', 'anfitrion', 'menu']
    success_url = reverse_lazy('casas')

class Casadelete(LoginRequiredMixin, DeleteView):
    model = Casa
    success_url = reverse_lazy('casas')
   
class Casaupdate(LoginRequiredMixin, UpdateView):
    model = Casa
    fields = ['calle' , 'altura', 'piso', 'departamento', 'localidad', 'horario', 'anfitrion', 'menu']
    success_url = reverse_lazy('casas')
   


#Login, registro y modificacion de usuario

def login_usuario(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "casas/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "casas/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "casas/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "casas/login.html", {"form":miForm}) 
       
    
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "casas/base.html")
    else:
        miForm =   RegistroForm()      
    return render(request, "casas/registro.html", {"form":miForm})


@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"casas/base.html")
        else:
            return render(request,"casas/editar_usuario.html", {'form': form, 'usuario': usuario.username})
    else:
        form = EditForm(instance=usuario)
    return render(request, "casas/editar_usuario.html", {'form': form, 'usuario': usuario.username})

#Avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

           
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

          
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

           
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"casas/base.html")
    else:
        form = AvatarForm()
    return render(request, "casas/agregarAvatar.html", {'form': form })
