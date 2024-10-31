from django.urls import path
from . import views # Importa as funções com as views definidas

urlpatterns = [
    #path('produtos/',views.buscar_produtos_get),
    #path('produtos/',views.buscar_produtos_get), # Associa a URL '/produtos' com a função buscar_produtos_get
    #path('cadastra_produto',views.cadastra_produto_post),
    #path('cadastra_produto',views.cadastra_produto_post),


    path('listar_produtos',views.buscar_todos_os_produtos),
    path('listar_produtos_template',views.buscar_produtos),
    path('cadastro_de_produtos',views.cadastrar_produto),    
    path('deletar', views.remover_produto),
    path('tupla_de_produtos_estaticos',views.produtos_estaticos),
    path('lista_de_roupas', views.lista_de_roupas),
    path('cadastro_produto_formulario', views.cadastrar_produtos_formulario, name='rota_de_cadsastrar_produtos'),
    path('alterar_produtos', views.atualizar_produto, name='alterar_produtos'),
]