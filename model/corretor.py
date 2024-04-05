from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model.base import Base

class Corretor(Base):

    __tablename__ = 'corretor'

    id = Column(Integer,primary_key=True, autoincrement=True, nullable=False)

    nome_corretor = Column(String(140), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    telefone = Column(String(11), nullable=True)