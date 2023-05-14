""" Views referentes as funcionalidades do aplicativo blogs """

""" IMPORTAÇOES DE MODULOS QUE FORAM USADOS """
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import Http404
from .models import Blog, Coment
from .forms import BlogForm, ComentForm
# Create your views here.

def index(request):
    """ Tela inicial mostra link para blogs """
    return render(request, 'blogs/index.html')

def blogs(request):
    """ View que mostra todos os blogs presentes no banco de dados """
    try:
        blogs = get_list_or_404(Blog)
        return render(request, 'blogs/blogs.html', {'blogs':blogs})
    except:
        return redirect('blogs:new_blog')
        # raise Http404("SEM BLOGS NO BANCO DE DADOS")

def blog(request, blog_id):
    """ Mostra um blog inico usando o parametro blog_id """
    blog = get_object_or_404(Blog, id=blog_id)
    coment = blog.coment_set.order_by('-date_added')#lista no template tem que passar o for
    context = {'blog':blog, 'coment':coment}
    return render(request, 'blogs/blog.html',context)

def new_blog(request):
    """ Cria um novo blog usando os forms do django no blogs/forms.py """
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    context = {'form':form}
    return render(request, 'blogs/new_blog.html', context)

def new_coment(request, blog_id):
    """ Cria um novo comentario para um blog especifico """
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method != 'POST':
        form = ComentForm()
    else:
        form = ComentForm(data=request.POST)
        if form.is_valid():
            new_coment = form.save(commit=False)
            new_coment.blog = blog
            new_coment.save()
            return redirect('blogs:blog', blog_id)

    context = {'blog':blog, 'form':form}
    return render(request, 'blogs/new_coment.html', context)

def edit_coment(request, coment_id):
    """ Edita um comentario ja existente usando o parametro coment_id """
    coment = get_object_or_404(Coment, id=coment_id)
    blog = coment.blog
    if request.method != 'POST':
        form = ComentForm(instance=coment)
    else:
        form = ComentForm(instance=coment, data=request.POST)#data=request.POST informaçoes do formulario no template em forma de post
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog.id)
    context = {'coment':coment, 'blog':blog, 'form':form}
    return render(request, 'blogs/edit_coment.html', context)

def edit_blog(request, blog_id):
    """ Edita um blog ja existente """
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    context = {'blog':blog, 'form':form}
    return render(request, 'blogs/edit_blog.html', context)

def delete_blog(request, blog_id):
    """ Deleta um blog existente usando o id = blog_id """
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('blogs:blogs')

def delete_coment(request, coment_id):
    """ Deleta um comenta existente usando o id = coment_id que foi recebido na url"""
    coment = get_object_or_404(Coment, id=coment_id)
    blog = coment.blog
    coment.delete()
    return redirect('blogs:blog', blog.id)
