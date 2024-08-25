from flask import Blueprint, render_template

vendas_route = Blueprint('vendas', __name__)

@vendas_route.route('/')
def home():
    return render_template('vendas.html')