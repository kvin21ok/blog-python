"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from BlogcitoPython.views import (index, PostList, CreatePost, 
                                    DetailPost, DeletePost, UpdatePost,
                                    UserSignUp, UserLogin, UserLogout,
                                    UpdateAvatar, UpdateUser, CreateMessage,
                                    MessageList, DetailMessage, DeleteMessage)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogcitopython/', index, name='blogcitopython_index'),
    path('blogcitopython/listar/', PostList.as_view(), name='blogcitopython_listar'),
    path('blogcitopython/crear/', CreatePost.as_view(), name='blogcitopython_crear'),
    path('blogcitopython/<int:pk>/detalle/', DetailPost.as_view(), name='blogcitopython_detalle'),
    path('blogcitopython/<int:pk>/borrar/', DeletePost.as_view(), name='blogcitopython_borrar'),
    path('blogcitopython/<int:pk>/actualizar/', UpdatePost.as_view(), name='blogcitopython_actualizar'),
    path('blogcitopython/signup/', UserSignUp.as_view(), name='blogcitopython_signup'),
    path('blogcitopython/login/', UserLogin.as_view(), name='blogcitopython_login'),
    path('blogcitopython/logout/', UserLogout.as_view(), name='blogcitopython_logout'),
    path('blogcitopython/avatars/<int:pk>/actualizar/', UpdateAvatar.as_view(), name='blogcitopython_actualizar_avatar'),
    path('blogcitopython/users/<int:pk>/actualizar/', UpdateUser.as_view(), name='blogcitopython_actualizar_usuario'),
    path('blogcitopython/mensajes/crear/', CreateMessage.as_view(), name='blogcitopython_crear_mensajes'),
    path('blogcitopython/mensajes/<int:pk>/detalle/', DetailMessage.as_view(), name='blogcitopython_detalle_mensajes'),
    path('blogcitopython/mensajes/listar/', MessageList.as_view(), name='blogcitopython_listar_mensajes'),
    path('blogcitopython/mensajes/<int:pk>/borrar/', DeleteMessage.as_view(), name='blogcitopython_borrar_mensajes'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)