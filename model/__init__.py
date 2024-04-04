from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os

from model.base import Base
from model.cliente import Cliente
from model.corretor import Corretor


db = "database/"

# Verificando se o path do banco de dados existe
# Caso não exista será criado
if not os.path.exists(db):
    os.makedirs(db)

# URL do banco de dados
db_url = 'sqlite:///%s/db.sqlite3' % db

# criando a engine do banco de dados
engine = create_engine(db_url, echo=False)

# instância do session
Session = sessionmaker(bind=engine)

#verificando se o banco já existe
if not database_exists(engine.url):
    create_database(engine.url)

#cadastrando tabelas no banco
Base.metadata.create_all(engine)