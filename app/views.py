from django.shortcuts import render, redirect
import json # importa os modulo json para trabalhar com dados em formato json
from django.http import JsonResponse, HttpResponseRedirect # A classe JasonResponse retorna os dados em formato Json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Produto
from .forms import ProdutoForm

# Lista incial de pridutos
lista_produtos = ['pao', 'queijo', 'coca cola']
prods = {
    "id": "1",
    "nome": 'Pão',
    "marca": 'Pão de Sal',
    "preco": 1.29,
    "estoque": 50, 
    }
    
    
# Exemplo de GET - Busca dado(s)
@csrf_exempt
def buscar_todos_os_produtos(request):
    print('Teste')
    produtos = Produto.objects.all().values()
    for produto in produtos:
        print(produto)
    
    # Esta view retorna a lista de produtos em formato json
    if request.method == 'GET': # Verifica se o metodo da requisição é GET
        return JsonResponse({'produtos' : lista_produtos}) # Retorna a lista de produtos com JSON - par chave:valor
    
    else: # Se não for GET retorna um erro 405 (Método não permitido)
        return JsonResponse({'erro': 'Metodo nao Permitido - Sou GET'})
    
@csrf_exempt
@require_http_methods(['PUT'])
def atualizar_produto(request, produto_id):
    try:
        # Tenta obter o livro com o ID fornecido
        produto = Produto.objects.get(id=produto_id)

        # Decodificar o JSON
        try:
            dados = json.loads(request.body)
        except json.JSONDecodeError as e:
            print('Erro ao decodificar JSON')
            return JsonResponse({'error':str(e), 'message' : 'Erro ao decodificar o JSON'}, status=400)
    
        # Atualiza os campos do livro 
        produto.nome = dados.get('nome')
        produto.marca = dados.get('marca')
        produto.preco = dados.get('preco')
        produto.estoque = dados.get('estoque')

        # Atualiza o Banco
        produto.save()
        print(produto)
        return JsonResponse({'message':'Produto atualizado com sucesso!!!'})

    # Se o id Fornecido não existir
    except: 
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

# Exemplo de Post - Inclui um dado(s)
@csrf_exempt
@require_http_methods(['POST'])
def cadastrar_produto(request):
        # Verifica se o corpo da requisição contem dados
    if not request.body:
        return JsonResponse({'error' : 'Dados Vazios'}, status=400)

    # Decodificar o JSON
    try:
        dados = json.loads(request.body)
    except json.JSONDecodeError as e:
        print('Erro ao decodificar JSON')
        return JsonResponse({'error':str(e), 'message' : 'Erro ao decodificar o JSON'}, status=400)

    # Validar campos obrigatorios
    required_fields = ['nome', 'marca','preco','estoque']
    for field in required_fields:
        if field not in dados:
            return JsonResponse({'error' : f'O campo {field} é obrigatorio'}, status=400)

    produto = Produto.objects.create(
        nome = dados.get('nome'),
        marca = dados.get('marca'),
        preco = dados.get('preco'),
        estoque = dados.get('estoque')
    )
    print(produto)
    return JsonResponse({'id':produto.id, 'message': 'Produto Adicionado com Sucesso!'}, status=201)


@csrf_exempt
def cadastrar_produtos_formulario(request):
    form = ProdutoForm(request.POST)

    if form.is_valid():
        produto = form.save()
        return HttpResponseRedirect("/produtos/listar_produtos_template")
    else:
        form = ProdutoForm()

    return render(request, 'app/template_produtos_formulario.html', {'forms' : form})

    

#Exemplo Delete
@csrf_exempt
def remover_produto(request):
    if request.method == 'DELETE':
        try:
            body = json.loads(request.body)  # Lê o corpo da requisição JSON
            produto_remover = body.get('nome')
            if produto_remover in lista_produtos:
                lista_produtos.remove(produto_remover)
                return JsonResponse({'mensagem': 'Produto removido', 'produtos': lista_produtos})
            else:
                return JsonResponse({'erro': 'Produto não encontrado'}, status=404)
            
        except json.JSONDecodeError:
            return JsonResponse({'erro': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'erro': 'Metodo nao permitido - Sou DELETE'}, status=405)
    

def produtos_estaticos(request):
    tupla_de_produtos_estatico = ('arroz', 'feijão', 'macarrão')
    return render(request, 'app/index.html', {'tupla_de_produtos' : tupla_de_produtos_estatico})



def lista_de_roupas(request):
    tupla_de_produtos_estatico = ('arroz', 'feijão', 'macarrão')

    roupas = [
        'Blusa',
        'Short', 
        'Camisa', 
        'Calça Jeans',
        'Vestido',
        'Bermuda',
    ]

    return render(request, 'app/index.html', {'tupla_de_produtos' : tupla_de_produtos_estatico, 'lista_de_roupas' : roupas})

def buscar_produtos(request):
    produtos = Produto.objects.all().values()
    for produto in produtos:
        print(produto)
    return render(request, 'app/template_produtos.html', {'produtos' : produtos})