from sqlalchemy import Column, String, ForeignKey, Integer
from model.base import Base


class Cliente(Base):

    __tablename__ = 'cliente'

    id = Column(Integer,primary_key=True, autoincrement=True, nullable=False)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    telefone = Column(String(11), nullable=True)
    nome_corretor = Column(String(140),  nullable=False)

    def __init__(self, nome, cpf, telefone, nome_corretor):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nome_corretor = nome_corretor