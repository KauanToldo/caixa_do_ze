from flask import Blueprint, render_template, request, url_for, redirect
from database.usuarios import USUARIOS

login_route = Blueprint('login', __name__)

@login_route.route('/')
def home():
    return render_template('login.html')

@login_route.route('/', methods=['POST'])
def check_login():
    email_input = request.form.get('email')
    senha_input = request.form.get('senha')

    usuario = next((u for u in USUARIOS if u['email'] == email_input), None)
    
    if usuario:
        if usuario['senha'] == senha_input:
            return redirect(url_for('vendas.home'))
        else:
            return('senha incorreta')
    else:
        return('usuario nao encontrado')
