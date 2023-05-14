""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


app_name = 'users'
urlpatterns = [
    #Pagina de login para entrar no sistema
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #Pagina de logout para deslogar do sistema
    path('logout/', views.logout_view, name='logout'),
    #Pagina para um novo user se cadastrar no sistema
    path('register/', views.register, name='register'),
]
