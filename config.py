import os.path
from jogoteca import app

SECRET_KEY = 'alura'   #senha para session

SQLALCHEMY_DATABASE_URI =  \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'root',
        servidor = 'localhost',
        database = 'jogoteca'
    )


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

