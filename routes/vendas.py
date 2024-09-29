from flask import Blueprint, render_template, request, redirect, url_for
from database.vendas import VENDAS
from database.estoque import ESTOQUE

vendas_route = Blueprint('vendas', __name__)

@vendas_route.route('/')
def home():
    qtd_vendas = len(VENDAS)
    produtos_estoque = [{'nome': prod['nome'], 'id': prod['id']} for prod in ESTOQUE]
    return render_template('vendas.html', qtd_vendas=qtd_vendas, vendas=VENDAS, produtos=produtos_estoque)


@vendas_route.route('/', methods=['POST'])
def inserirVenda():
    dados = request.json
    if any(venda['produto'] == dados['produto'] and venda['data'] == dados['data'] for venda in VENDAS):
        return {'message': 'Venda já existe.'}, 400
    produto = next((prod for prod in ESTOQUE if prod['nome'] == dados['produto']), None)

    if not produto:
        return {'message': 'Produto não encontrado no estoque.'}, 404
    
    if produto['quantidade'] < int(dados['quantidade']):
        return {'message': 'Quantidade insuficiente em estoque.'}, 400
    
    
    novo_venda = {
        "id": len(VENDAS) + 1,
        "produto": dados['produto'],
        "data": dados['data'],
        "quantidade": dados['quantidade'],
        "valor_uni": produto['valor_venda'],
        "valor_total": int(produto['valor_venda']) * int(dados['quantidade'])
    }

    VENDAS.append(novo_venda)
    produto['quantidade'] -= int(dados['quantidade'])
    return render_template('itemVenda.html', venda=novo_venda)
    
@vendas_route.route('/<int:venda_id>/delete', methods=['DELETE'])
def deleteVenda(venda_id):
    global VENDAS
    VENDAS = [u for u in VENDAS if u['id'] != venda_id]
    qtd_vendas = len(VENDAS)
    return render_template('vendas.html', qtd_vendas=qtd_vendas, vendas=VENDAS)