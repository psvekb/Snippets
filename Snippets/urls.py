from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippet/<int:id>', views.snippet, name='snippet'),
    path('snippet/<int:id>/delete', views.snippet_delete, name='snippet_delete'),
    path('snippet/<int:id>/edit', views.snippet_edit, name='snippet_edit'),
    path('snippets/list', views.snippets_page, name='snippets_list'),
    path('snippets/list/my', views.snippets_page, name='snippets_list_my'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('snippets/create', views.create_snippet, name='create-snippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 