from django.http import Http404
from django.shortcuts import render, redirect
from .models import Snippet
from MainApp.forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов', 'snippets' : Snippet.objects.all(), 'snippets_count':Snippet.objects.count()}
    return render(request, 'pages/view_snippets.html', context)

def snippet(request, id):
    try:
        snippet = Snippet.objects.get(id = id)
        
        # colors = item.colors.all()
        # print(f'{colors=}')
    except:
        return Http404(f'Сниппет c {id = } не найден')
    
    print(snippet)    
    context = {'pagename': 'Сниппет', 'snippet' : snippet}
    return render(request, 'pages/snippet.html', context)

def add_snippet_page(request):
    form = SnippetForm()
    return render(request, 'add_snippet.html', {'form': form})

def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("redirect_url")
    return render(request,'add_snippet.html',{'form': form})    