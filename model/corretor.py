from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from model.base import Base

class Corretor(Base):

    __tablename__ = 'corretor'
    nome_corretor = Column(String(140), primary_key=True)
    clientes = relationship('Cliente', backref='corretor')

    def __init__(self, corretor):
        self.nome_corretor = corretor
