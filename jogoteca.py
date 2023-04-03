from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)  # faz referencia a esse proprio arquivo, ele garante quue isso vai fazer rodar a apicacao.
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from views_game import *
from views_user import *
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

