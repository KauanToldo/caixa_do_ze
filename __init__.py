from flask import Flask
from routes.vendas import vendas_route
from routes.estoque import estoque_route
from routes.dashboard import dashboard_route
from routes.cadastro import cadastro_route
from routes.login import login_route

app = Flask(__name__)
app.config['SECRET_KEY']='dev'

app.register_blueprint(vendas_route, url_prefix="/vendas")
app.register_blueprint(estoque_route, url_prefix="/estoque")
app.register_blueprint(dashboard_route, url_prefix="/dashboard")
app.register_blueprint(cadastro_route, url_prefix="/cadastro")
app.register_blueprint(login_route, url_prefix="/login")

if __name__ == '__main__':
    app.run(debug=True) 
