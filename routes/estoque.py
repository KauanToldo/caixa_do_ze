from flask import Blueprint, render_template

estoque_route = Blueprint('estoque', __name__)

@estoque_route.route('/')
def home():
    return render_template('estoque.html')