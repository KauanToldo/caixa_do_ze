from flask import Blueprint, render_template, request, redirect, url_for
from database.vendas import VENDAS
from database.estoque import ESTOQUE
from database.compras import COMPRAS

dashboard_route = Blueprint('dashboard', __name__)

@dashboard_route.route('/')
def home():
    qtd_vendas = len(VENDAS)
    qtd_estoque = len(ESTOQUE)
    valor_obtido = sum(venda['valor_total'] for venda in VENDAS)
    valor_gasto = sum(int(produto['valor_compra']) * int(produto['quantidade']) for produto in COMPRAS)
    qtd_produtos = sum(int(produto['quantidade']) for produto in COMPRAS)
    qtd_produtos_vendidos = sum(int(venda['quantidade']) for venda in VENDAS)
    lucro =  valor_obtido - valor_gasto


    return render_template('dashboard.html', qtd_vendas=qtd_vendas, qtd_estoque=qtd_estoque, valor_obtido=valor_obtido, valor_gasto=valor_gasto, qtd_produtos=qtd_produtos, qtd_produtos_vendidos=qtd_produtos_vendidos, lucro=lucro)