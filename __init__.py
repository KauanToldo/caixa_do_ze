from flask import Flask
from routes.vendas import vendas_route

app = Flask(__name__)
app.config['SECRET_KEY']='dev'

app.register_blueprint(vendas_route)

if __name__ == '__main__':
    app.run(debug=True) 
