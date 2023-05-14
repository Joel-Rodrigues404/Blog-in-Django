""" Configurações do site para admins """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.contrib import admin
from .models import Blog, Coment
# Register your models here.

class ListingBlogs(admin.ModelAdmin):
    """ Class para ajudar na visualizaçao dos dados no site de admin """
    list_display = ('id', 'title', 'text', 'date_added')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('date_added', )
    # list_editable = ('title',)
    list_per_page = 5

class ListingComents(admin.ModelAdmin):
    """ Class para ajudar na visualizaçao dos dados no site de admin """
    list_display = ('id', 'blog', 'coment', 'date_added')
    list_display_links = ('id', 'blog','coment')
    search_fields = ('blog', 'coment',)
    list_filter = ('date_added', )
    # list_editable = ('title',)
    list_per_page = 5

#Onde são registrados os models para apareçerem no site para admins
admin.site.register(Blog, ListingBlogs)
admin.site.register(Coment, ListingComents)
