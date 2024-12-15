from django.http import Http404
from django.shortcuts import render, redirect
from .models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов', 'snippets' : Snippet.objects.all(), 'snippets_count':Snippet.objects.count()}
    return render(request, 'pages/view_snippets.html', context)
