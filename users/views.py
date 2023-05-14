""" Views referentes as funcionalidades do aplicativo blogs """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, BadHeaderError

# Create your views here.

def logout_view(request):
    """ View que faz o logout do usuario para sair do sistema """
    auth.logout(request) #Função embutida do django que faz logout
    return redirect('blogs:index')

def register(request):
    """ View faz a criação de um novo usuario """
    if request.method == 'GET':
        #Inicialmente cria o formulario e branco se o metodo for get
        form = UserCreationForm()
    elif request.method == 'POST':
        #recebe as informaçoes se o metodo for get no form pela request.POST
        form = UserCreationForm(data=request.POST)
        #Se o formulario for valido entra no if
        if form.is_valid():
            #cria uma nova instancia new user que recebe as info do formulario
            new_user = form.save()
            #Cria o novo usuario com as informaçoes do form
            #São usados parametros obrigatorios para a criação de um user como username
            authenticated_user = auth.authenticate(
                username = new_user.username,
                password = request.POST['password1']
            )
            #Apos o objeto do usuario ser criado ele e logado automaticamente com a função abaixo
            auth.login(request, authenticated_user)
            return redirect('blogs:index')
    else:
        return BadHeaderError('Falha ao registrar novo usuario tente novamente')
    context = {'form':form}
    return render(request, 'users/register.html', context)