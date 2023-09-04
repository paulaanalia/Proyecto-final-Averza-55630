from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
   path('', home, name="home"),
   path('about/', about, name="about"),
   path('comofunciona/', como_funciona, name="comofunciona"),
   
   path('casabuscar/', casa_buscar, name="casabuscar"),
   path('casabuscar2/', casa_buscar2, name="casabuscar2"),

   path('casas/', Casaslist.as_view(), name="casas"),
   path('create_casa/', Casacreate.as_view() , name="create_casa" ),    
   path('delete_casa/<int:pk>/', Casadelete.as_view(), name="delete_casa" ),
   path('update_casa/<int:pk>/', Casaupdate.as_view(), name="update_casa" ),
   

   path('login/', login_usuario, name="login" ),
   path('logout/', LogoutView.as_view(template_name ='casas/logout.html'), name="logout"),
   path('registro/', register, name="registro" ),
   path('editar_usuario/', editar_usuario, name="editar_usuario" ),
   path('agregar_avatar/', agregarAvatar, name="agregar_avatar" )
]