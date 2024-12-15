from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippet/<int:id>', views.snippet, name='snippet'),
    path('snippets/list', views.snippets_page, name='list_snippets'),
    path('snippets/create', views.create_snippet, name='create-snippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 