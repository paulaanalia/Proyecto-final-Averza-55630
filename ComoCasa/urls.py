
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ComoCasa import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('casas.urls')),
    ]
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('casas.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)