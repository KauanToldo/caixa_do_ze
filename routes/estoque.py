from flask import Blueprint, render_template, request, redirect, url_for
from database.estoque import ESTOQUE
from database.compras import COMPRAS

estoque_route = Blueprint('estoque', __name__)

@estoque_route.route('/')
def home():
    qtd_produtos = len(ESTOQUE)
    return render_template('estoque.html', qtd_produtos = qtd_produtos, estoque=ESTOQUE)

@estoque_route.route('/<int:produto_id>/delete', methods=['DELETE'])
def deleteProduto(produto_id):
    global ESTOQUE
    ESTOQUE = [u for u in ESTOQUE if u['id'] != produto_id]
    qtd_produtos = len(ESTOQUE)
    return render_template('estoque.html', qtd_produtos = qtd_produtos, estoque=ESTOQUE)

@estoque_route.route('/', methods=['POST'])
def inserirProduto():
    dados=request.json
    if any(produto['nome'] == dados['nome'] for produto in ESTOQUE):
        return {'message': 'Produto já existe.'}, 400
    novo_produto={
        "id":len(ESTOQUE)+1,
        "nome":dados['nome'],
        "quantidade":dados['quantidade'],
        "valor_venda":dados['preco_compra'],
        "valor_compra":dados['preco_venda'],
        "valor_total": int(dados['preco_compra']) *  int(dados['quantidade'])
    }
    ESTOQUE.append(novo_produto)
    COMPRAS.append(novo_produto)
    return render_template('itemEstoque.html', produto=novo_produto)

@estoque_route.route('/<int:produto_id>/edit', methods=['GET'])
def editProduto(produto_id):
    produto = next((u for u in ESTOQUE if u['id'] == produto_id), None)
    if produto is None:
        return "Produto não encontrado", 404
    return render_template('formEstoque.html', produto=produto)


@estoque_route.route('/<int:produto_id>/update', methods=['PUT'])
def updateProduto(produto_id):
    produto_editado = None
    data = request.json
    for u in ESTOQUE:
        if u['id'] == produto_id:
            u['nome'] = data['nome']
            u['quantidade'] = data['quantidade']
            u['valor_venda'] = data['valor_venda']
            u['valor_compra'] = data['valor_compra']
            u['valor_total'] = data['valor_total']
            produto_editado = u
    return render_template('itemProduto.html', produto=produto_editado)


@estoque_route.route('/new', methods=['GET'])
def formEstoque():
    return render_template('formEstoque.html')