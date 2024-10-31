from django.urls import path
from bookmanager.views import index, criar_livro, listar_livros, atualizar_livro


urlpatterns = [
    #path('', index, name='index'),
    path('adicionar_livro', criar_livro, name='criar_livro'),
    path('listar_livros', listar_livros, name='listar_livros'),
    path('atualizar_livro', atualizar_livro, name='atualizar_livro'),
]