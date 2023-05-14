""" Models referentes ao Aplicativo blogs """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.db import models

# Create your models here.
class Blog(models.Model):
    """Modelo referente a todos os blogs"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    """ Passa a nomear a instancia no plural quando se tem mais de um blog """
    class Meta:
        verbose_name_plural = 'Blogs'

    def __str__(self) -> str:
        return self.title
    
class Coment(models.Model):
    """ Modelo referente a um comentario para um blog especifico ultilizando o campo blog para a relaçao """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    coment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    """ Passa a nomear a instancia no plural quando se tem mais de um comentario """
    class Meta:
        verbose_name_plural = 'coments'
    
    def __str__(self) -> str:
        return self.coment