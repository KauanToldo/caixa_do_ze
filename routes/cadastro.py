from flask import Blueprint, render_template, request, url_for, redirect
from database.usuarios import USUARIOS

cadastro_route = Blueprint('cadastro', __name__)

@cadastro_route.route('/')
def home():
    return render_template('cadastro.html')

@cadastro_route.route('/', methods=['POST'])
def cadastroUsuario():
    email = request.form.get('email')
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    novo_usuario={
        "id":len(USUARIOS)+1,
        "nome":nome,
        "email":email,
        "senha":senha
    }
    USUARIOS.append(novo_usuario)
    return redirect(url_for('vendas.home'))