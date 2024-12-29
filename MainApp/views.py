from django.http import Http404, HttpResponseNotFound,HttpResponse
from django.shortcuts import render, redirect
from .models import Snippet
from .forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.db.models import Q

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username =", username)
        print("password =", password)
        user = auth.authenticate(request, username=username,
        password=password)
        if user is not None:
            auth.login(request, user)
        else:
        # Return error message
           pass
    return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')


     

def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета', 'form': form}
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect("snippets_list")
        return render(request,'pages/add_snippet.html',{'form': form})  

def snippets_page(request):
    print( request.path)
    print( request.user.id)
    if request.path == '/snippets/list/my':
        snippets = Snippet.objects.all().filter(user_id=request.user.id)
    else:
        snippets = Snippet.objects.all().exclude(~Q(user_id=request.user.id), private=True)
    snippets_count= snippets.count()
    context = {'pagename': 'Просмотр сниппетов', 'snippets' : snippets, 'snippets_count':snippets_count}
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
    return redirect('snippets_list')

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
            print(f'{data_form=}')
            snippet.name = data_form['name']
            # snippet.lang = data_form['lang']
            snippet.creation_date = data_form['creation_date']
            snippet.code = data_form['code']
            snippet.private = data_form['private']
            snippet.save()
            return redirect('snippets_list')