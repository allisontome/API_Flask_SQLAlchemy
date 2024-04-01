from sqlalchemy import Column, String, ForeignKey
from model.base import Base


class Cliente(Base):

    __tablename__ = 'cliente'

    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), primary_key=True)
    telefone = Column(String(11), nullable=True)
    nome_corretor = Column(String(140), ForeignKey('corretor.nome_corretor'), nullable=False)

    def __init__(self, nome, cpf, telefone, nome_corretor):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nome_corretor = nome_corretor