""" Urls do aplicativo blogs """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.urls import path
from . import views

#Serve para simplificar as rotas do projeto usa o padrão 'blogs:name da url' e pode usar um parametro como id
app_name = 'blogs' 
urlpatterns = [
    #Pagina Inicial
    path('', views.index, name='index'),
    #Mostra Todos os Blogs
    path('blogs/', views.blogs, name='blogs'),
    #Mostra uma Pagina detalhada para um blog especifico usa o parametro de url blog_id que e um Int
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    #Pagina para criar um novo Blog
    path('new_blog/', views.new_blog, name='new_blog'),
    #Pagina para criar um novo comentario usa o parametro de url blog_id que e um Int para especificar a qual blog esse comentario se refere
    path('new_coment/<int:blog_id>', views.new_coment, name='new_coment'),
    #Pagina para editar um comentario
    path('edit_coment/<int:coment_id>', views.edit_coment, name='edit_coment'),
    #Pagina para editar um blog especifico
    path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
    #Url para deletar um comentario
    path('delete_coment/<int:coment_id>', views.delete_coment, name='delete_coment'),
    #Url para deletar um blog 
    path('delete_blog/<int:blog_id>', views.delete_blog, name='delete_blog'),
]
