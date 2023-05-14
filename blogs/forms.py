""" Models para Criaçao de formularios """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django import forms
from .models import Blog, Coment

#Classes que definem modelos de formularios que herdam de forms.ModelForm

class BlogForm(forms.ModelForm):
    """ Formulario de Blog """
    class Meta:
        model = Blog #Define o Model que sera usado para o form
        fields = ['title','text'] #define os campos do Model que serão usados no form
        labels = {'title':'title', 'text':'text'} #define o nome que aparece na box
        widgets = {'text':forms.Textarea(attrs={'cols':80})} #Define como vai ser apresentado a caisa de texto

class ComentForm(forms.ModelForm):
    """ Formulario de coment """
    class Meta:
        model = Coment #Define o Model que sera usado para o form
        fields = ['coment'] #define os campos do Model que serão usados no form
        labels = {'coment':'coment'} #define o nome que aparece na box
        widgets = {'coment':forms.Textarea(attrs={'cols':80})} #Define como vai ser apresentado a caisa de texto
