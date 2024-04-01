from sqlalchemy import String, Integer, Column, ForeignKey, create_engine
from sqlalchemy.orm import Mapped, Session, relationship
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Corretor(Base):

    __tablename__ = 'corretor'
    nome_corretor = Column(String(140), primary_key=True)
    clientes = relationship('cliente')

class Cliente(Base):

    __tablename__ = 'cliente'

    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), primary_key=True)
    telefone = Column(String(11), nullable=True)
    nome_corretor = Column(String(140), ForeignKey('corretor.nome_corretor'), nullable=False)


db = "database/"

if not os.path.exists(db):
    os.makedirs(db)


db_url = 'sqlite:///%s/db.sqlite3' % db

engine = create_engine(db_url, echo=False)

session = Session(engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)