from django.http import Http404, HttpResponseNotFound,HttpResponse
from django.shortcuts import render, redirect
from .models import Snippet
from .forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("list_snippets")
    return render(request,'pages/add_snippet.html',{'form': form})  

def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов', 'snippets' : Snippet.objects.all(), 'snippets_count':Snippet.objects.count()}
    return render(request, 'pages/view_snippets.html', context)

def snippet(request, id):
    try:
        snippet = Snippet.objects.get(id = id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Сниппет c {id = } не найден')
    else:
        context = {'pagename': 'Сниппет', 'snippet' : snippet, 'type':'view'}
        return render(request, 'pages/snippet.html', context)


def snippet_delete(request, id:int):
    if request.method == "POST":
        snippet =Snippet.objects.get (id=id) # Snippet.objects.get(id = id)
        snippet.delete()
    return redirect('list_snippets')

def snippet_edit(request, id:int):
    try:
        snippet = Snippet.objects.get(id = id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Сниппет c {id = } не найден')
    else:
        if request.method == 'GET':
            context = {'pagename': 'Сниппет', 'snippet' : snippet, 'type':'edit'}
            return render(request, 'pages/snippet.html', context)
        
        if request.method == 'POST':
            data_form = request.POST
            snippet.name = data_form['name']
            # snippet.lang = data_form['lang']
            snippet.creation_date = data_form['creation_date']
            snippet.code = data_form['code']
            snippet.save()
            return redirect('list_snippets')