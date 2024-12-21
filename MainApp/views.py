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
        
        # colors = item.colors.all()
        # print(f'{colors=}')
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Сниппет c {id = } не найден')
    else:
        print(snippet)    
        context = {'pagename': 'Сниппет', 'snippet' : snippet}
        return render(request, 'pages/snippet.html', context)

# def create_snippet(request):
#     from pprint import pprint
#     if request.method == "POST":
#         pprint(request.POST)
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("list_snippets")
#     return render(request,'pages/add_snippet.html',{'form': form})    